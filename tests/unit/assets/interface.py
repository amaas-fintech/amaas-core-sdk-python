# coding=utf-8

import random
import unittest

from amaascore.assets.asset import Asset
from amaascore.assets.bond_option import BondOption
from amaascore.assets.foreign_exchange import ForeignExchange
from amaascore.assets.interface import AssetsInterface
from amaascore.tools.generate_asset import generate_asset, generate_foreignexchange


class AssetsInterfaceTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.assets_interface = AssetsInterface()
        self.asset_manager_id = random.randint(1, 2**31-1)
        self.asset = generate_asset(asset_manager_id=self.asset_manager_id)
        self.asset_id = self.asset.asset_id

    def tearDown(self):
        pass

    def test_New(self):
        self.assertIsNone(self.asset.created_time)
        asset = self.assets_interface.new(self.asset)
        # TODO - this should be populated by the New call.
        #self.assertIsNotNone(asset.created_time)
        self.assertEqual(asset.asset_id, self.asset_id)

    def test_Amend(self):
        asset = self.assets_interface.new(self.asset)
        self.assertEqual(asset.version, 1)
        asset.description = 'TEST'
        asset = self.assets_interface.amend(asset)
        self.assertEqual(asset.description, 'TEST')
        self.assertEqual(asset.version, 2)

    def test_Retrieve(self):
        self.assets_interface.new(self.asset)
        fx = generate_foreignexchange()
        fx = self.assets_interface.new(fx)
        asset = self.assets_interface.retrieve(self.asset.asset_manager_id, self.asset.asset_id)
        fx = self.assets_interface.retrieve(fx.asset_manager_id, fx.asset_id)
        self.assertEqual(type(asset), Asset)
        self.assertEqual(type(fx), ForeignExchange)

    def test_Deactivate(self):
        self.assets_interface.new(self.asset)
        self.assets_interface.deactivate(self.asset.asset_manager_id, self.asset.asset_id)
        asset = self.assets_interface.retrieve(self.asset.asset_manager_id, self.asset.asset_id)
        self.assertEqual(asset.asset_id, self.asset_id)
        self.assertEqual(asset.asset_status, 'Inactive')

    def test_Search(self):
        all_assets = self.assets_interface.search()
        random_asset_index = random.randint(0, len(all_assets)-1)
        asset_manager_id = all_assets[random_asset_index].asset_manager_id
        asset_manager_assets = [asset for asset in all_assets if asset.asset_manager_id == asset_manager_id]
        assets = self.assets_interface.search(asset_manager_ids=[asset_manager_id])
        self.assertEqual(len(assets), len(asset_manager_assets))

    def test_AssetsByAssetManager(self):
        all_assets = self.assets_interface.search()
        random_asset_index = random.randint(0, len(all_assets)-1)
        asset_manager_id = all_assets[random_asset_index].asset_manager_id
        asset_manager_assets = [asset for asset in all_assets if asset.asset_manager_id == asset_manager_id]
        assets = self.assets_interface.assets_by_asset_manager(asset_manager_id=asset_manager_id)
        self.assertEqual(len(assets), len(asset_manager_assets))

    def test_ChildrenPopulated(self):
        asset = self.assets_interface.new(self.asset)
        retrieved_asset = self.assets_interface.retrieve(asset_manager_id=self.asset_manager_id,
                                                         asset_id=self.asset_id)
        self.assertGreater(len(asset.references), 0)
        self.assertEqual(asset.references, retrieved_asset.references)

    def test_Unicode(self):
        unicode_description = u'日本語入力'
        self.asset.description = unicode_description
        asset = self.assets_interface.new(self.asset)
        self.assertEqual(asset.description, unicode_description)

if __name__ == '__main__':
    unittest.main()
