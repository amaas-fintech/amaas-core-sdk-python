# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import random
import unittest

from amaascore.config import DEFAULT_LOGGING
from amaascore.corporate_actions.interface import CorporateActionsInterface
from amaascore.tools.generate_corporate_action import generate_corporate_action

import logging.config
logging.config.dictConfig(DEFAULT_LOGGING)


class CorporateActionsInterfaceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
        cls.corporate_actions_interface = CorporateActionsInterface()

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.corporate_action = generate_corporate_action()
        self.corporate_action_id = self.corporate_action.corporate_action_id

    def tearDown(self):
        pass

    def test_New(self):
        self.assertIsNone(self.corporate_action.created_time)
        corporate_action = self.corporate_actions_interface.new(self.corporate_action)
        # TODO - this should be populated by the New call.
        #self.assertIsNotNone(corporate_action.created_time)
        self.assertEqual(corporate_action.corporate_action_id, self.corporate_action_id)

    def test_Amend(self):
        corporate_action = self.corporate_actions_interface.new(self.corporate_action)
        self.assertEqual(corporate_action.version, 1)
        corporate_action.asset_id = 'TEST'
        corporate_action = self.corporate_actions_interface.amend(corporate_action)
        self.assertEqual(corporate_action.asset_id, 'TEST')
        self.assertEqual(corporate_action.version, 2)

    def test_Retrieve(self):
        self.corporate_actions_interface.new(self.corporate_action)
        corporate_action = self.corporate_actions_interface.retrieve(self.corporate_action.asset_manager_id,
                                                                     self.corporate_action.corporate_action_id)
        self.assertEqual(corporate_action.corporate_action_id, self.corporate_action_id)

    def test_Cancel(self):
        self.corporate_actions_interface.new(self.corporate_action)
        self.corporate_actions_interface.cancel(self.corporate_action.asset_manager_id,
                                                self.corporate_action.corporate_action_id)
        corporate_action = self.corporate_actions_interface.retrieve(self.corporate_action.asset_manager_id,
                                                                     self.corporate_action.corporate_action_id)
        self.assertEqual(corporate_action.corporate_action_id, self.corporate_action_id)
        self.assertEqual(corporate_action.corporate_action_status, 'Cancelled')

    def test_Search(self):
        all_corporate_actions = self.corporate_actions_interface.search()
        random_index = random.randint(0, len(all_corporate_actions)-1)
        asset_manager_id = all_corporate_actions[random_index].asset_manager_id
        asset_manager_corporate_actions = [corporate_action for corporate_action in all_corporate_actions
                                           if corporate_action.asset_manager_id == asset_manager_id]
        corporate_actions = self.corporate_actions_interface.search(asset_manager_ids=[asset_manager_id])
        self.assertEqual(len(corporate_actions), len(asset_manager_corporate_actions))

    def test_CorporateActionsByAssetManager(self):
        all_corporate_actions = self.corporate_actions_interface.search()
        random_index = random.randint(0, len(all_corporate_actions)-1)
        asset_manager_id = all_corporate_actions[random_index].asset_manager_id
        asset_manager_corporate_actions = [corporate_action for corporate_action in all_corporate_actions
                                           if corporate_action.asset_manager_id == asset_manager_id]
        corporate_actions = self.corporate_actions_interface.corporate_actions_by_asset_manager(asset_manager_id)
        self.assertEqual(len(corporate_actions), len(asset_manager_corporate_actions))

    def test_Unicode(self):
        unicode_description = '日本語入力'
        self.corporate_action.description = unicode_description
        corporate_action = self.corporate_actions_interface.new(self.corporate_action)
        self.assertEqual(corporate_action.description, unicode_description)

if __name__ == '__main__':
    unittest.main()
