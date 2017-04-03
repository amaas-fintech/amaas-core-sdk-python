from __future__ import absolute_import, division, print_function, unicode_literals

import random
import unittest

from amaascore.asset_managers.asset_manager import AssetManager
from amaascore.asset_managers.interface import AssetManagersInterface
from amaascore.asset_managers.relationship import Relationship
from amaascore.tools.generate_asset_manager import generate_asset_manager, generate_relationship


class AssetManagersInterfaceTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_managers_interface = AssetManagersInterface()

    def tearDown(self):
        pass

    def test_New(self):
        asset_manager = generate_asset_manager()
        asset_manager = self.asset_managers_interface.new(asset_manager)
        self.assertEqual(type(asset_manager), AssetManager)

    def test_SearchAndRetrieve(self):
        all_asset_managers = self.asset_managers_interface.search()
        random_index = random.randint(0, len(all_asset_managers)-1)
        asset_manager = all_asset_managers[random_index]
        retrieved_manager = self.asset_managers_interface.retrieve(asset_manager_id=asset_manager.asset_manager_id)
        self.assertEqual(retrieved_manager, asset_manager)

    def test_NewRelationship(self):
        asset_manager_id = random.randint(1, 2**31-1)
        relationship = generate_relationship(asset_manager_id=asset_manager_id)
        relationship = self.asset_managers_interface.new_relationship(relationship)
        self.assertEqual(type(relationship), Relationship)

if __name__ == '__main__':
    unittest.main()
