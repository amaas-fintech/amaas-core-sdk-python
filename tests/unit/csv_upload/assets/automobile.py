import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.assets.automobile import AutomobileUploader
from amaascore.assets.automobile import Automobile
from amaascore.tools.csv_tools import objects_to_csv_stream

class EquityUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'AutomobileUploaderTest.csv'
        self.asset_id = 'US9IZ3235T'

    def tearDown(self):
        pass

    def test_AutomobileUploadDownload(self):
        AutomobileUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile)
        AutomobileUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=[self.asset_id])

if __name__ == '__main__':
    unittest.main()