import unittest
import csv
import random

from amaascore.csv_upload.assets.equity import EquityUploader
from amaascore.assets.equity import Equity
from amaascore.tools.csv_tools import *

class EquityUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        #self.EquityUploader = EquityUploader()
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'EquityUploaderTest.csv'

    def tearDown(self):
        pass

    def test_EquityUploadDownload(self):
        EquityUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile)
        EquityUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=[123])

if __name__ == '__main__':
    unittest.main()
