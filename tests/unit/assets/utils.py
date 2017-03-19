from __future__ import absolute_import, division, print_function, unicode_literals

import os
import os.path
import tempfile
import unittest


from amaascore.assets.asset import Asset
from amaascore.assets.utils import json_to_asset, assets_to_csv, assets_to_csv_stream, csv_filename_to_assets, \
    csv_stream_to_assets
from amaascore.tools.generate_asset import generate_asset


class AssetUtilsTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure

    def tearDown(self):
        pass

    def test_JsonToAsset(self):
        asset = generate_asset()
        json_asset = asset.to_json()
        gen_asset = json_to_asset(json_asset)
        self.assertEqual(gen_asset, asset)

    def test_AssetsToCSV(self):
        filename = os.path.join(tempfile.gettempdir(), 'test.csv')
        assets = [generate_asset() for i in range(5)]
        assets_to_csv(assets=assets, filename=filename)
        # Read the file back out again
        with open(filename, 'r') as temp_file:
            data = temp_file.readlines()
        self.assertEqual(len(data), 6)  # 5 assets + header
        os.remove(filename)

    def test_AssetsToCSVStream(self):
        file_desc, temp_filepath = tempfile.mkstemp()
        assets = [generate_asset() for i in range(5)]
        with open(temp_filepath, 'w') as temp_file:
            assets_to_csv_stream(assets=assets, stream=temp_file)
        # Read the file back out again
        with open(temp_filepath, 'r') as temp_file:
            data = temp_file.readlines()
        self.assertEqual(len(data), 6)  # 5 assets + header
        os.close(file_desc)
        os.remove(temp_filepath)

    def test_FilenameToAssets(self):
        # Generate file
        filename = os.path.join(tempfile.gettempdir(), 'test.csv')
        assets = [generate_asset() for i in range(5)]
        assets_to_csv(assets=assets, filename=filename)
        assets = csv_filename_to_assets(filename)
        self.assertEqual(len(assets), 5)
        self.assertEqual(type(assets[0]), Asset)
        os.remove(filename)

    def test_StreamToAssets(self):
        # Generate file
        filename = os.path.join(tempfile.gettempdir(), 'test.csv')
        assets = [generate_asset() for i in range(5)]
        assets_to_csv(assets=assets, filename=filename)
        with open(filename, 'r') as stream:
            assets = csv_stream_to_assets(stream)
        self.assertEqual(len(assets), 5)
        self.assertEqual(type(assets[0]), Asset)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
