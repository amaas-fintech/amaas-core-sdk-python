import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.assets.warrants import WarrantUploader
from amaascore.assets.warrants import Warrant
from amaascore.tools.csv_tools import objects_to_csv_stream

class WarrantUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'WarrantsUploaderTest.csv'
        #self.asset_id = 'AGDJSA2T'
        self.asset_ids = []
        for i in range(2):
                self.asset_ids.append(random_string(8))

    def tearDown(self):
        pass

    def test_WarrantUploadDownload(self):
        for asset_id in self.asset_ids:
            WarrantUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile, asset_id=asset_id)
        WarrantUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=self.asset_ids)

if __name__ == '__main__':
    unittest.main()