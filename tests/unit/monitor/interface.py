# coding=utf-8

import random
import unittest

from amaascore.monitor.interface import MonitorInterface
from amaascore.tools.generate_monitor_item import generate_item


class MonitorInterfaceTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.monitor_interface = MonitorInterface()
        self.item = generate_item()
        self.item_id = self.item.item_id

    def tearDown(self):
        pass

    def test_New(self):
        self.assertIsNone(self.item.created_time)
        item = self.monitor_interface.new_item(self.item)
        # TODO - this should be populated by the New call.
        #self.assertIsNotNone(item.created_time)
        self.assertEqual(item.item_id, self.item_id)

    def test_Retrieve(self):
        self.monitor_interface.new_item(self.item)
        item = self.monitor_interface.retrieve_item(self.item.asset_manager_id, self.item.item_id)
        self.assertEqual(item.item_id, self.item_id)

    def test_Resubmit(self):
        self.monitor_interface.new_item(self.item)
        item = self.monitor_interface.resubmit_item(self.item.asset_manager_id, self.item.item_id)
        self.assertEqual(item.item_id, self.item_id)
        self.assertEqual(item.item_status, 'Resubmitted')
        self.assertEqual(item.version, 2)

    def test_Close(self):
        self.monitor_interface.new_item(self.item)
        self.monitor_interface.close_item(self.item.asset_manager_id, self.item.item_id)
        item = self.monitor_interface.retrieve_item(self.item.asset_manager_id, self.item.item_id)
        self.assertEqual(item.item_id, self.item_id)
        self.assertEqual(item.item_status, 'Closed')

    def test_Search(self):
        all_items = self.monitor_interface.search_items()
        random_item_index = random.randint(0, len(all_items)-1)
        asset_manager_id = all_items[random_item_index].asset_manager_id
        asset_manager_items = [item for item in all_items if item.asset_manager_id == asset_manager_id]
        items = self.monitor_interface.search_items(asset_manager_ids=[asset_manager_id])
        self.assertEqual(len(items), len(asset_manager_items))

    def test_ItemsByAssetManager(self):
        all_items = self.monitor_interface.search_items()
        random_item_index = random.randint(0, len(all_items)-1)
        asset_manager_id = all_items[random_item_index].asset_manager_id
        asset_manager_items = [item for item in all_items if item.asset_manager_id == asset_manager_id]
        items = self.monitor_interface.items_by_asset_manager(asset_manager_id=asset_manager_id)
        self.assertEqual(len(items), len(asset_manager_items))

    def test_Unicode(self):
        unicode_message = u'日本語入力'
        self.item.message = unicode_message
        item = self.monitor_interface.new_item(self.item)
        self.assertEqual(item.message, unicode_message)

if __name__ == '__main__':
    unittest.main()
