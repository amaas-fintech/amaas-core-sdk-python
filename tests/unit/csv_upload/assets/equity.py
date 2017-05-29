import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.assets.equity import EquityUploader
from amaascore.assets.equity import Equity
from amaascore.tools.csv_tools import objects_to_csv_stream

class EquityUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'EquityUploaderTest.csv'
        self.asset_id = random_string(8)

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        EquityUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id,
                                csvpath=self.csvfile, asset_id=self.asset_id)
        EquityUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=[self.asset_id])

if __name__ == '__main__':
    unittest.main()