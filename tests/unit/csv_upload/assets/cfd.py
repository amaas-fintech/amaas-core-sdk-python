import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.assets.cfd import CFDUploader
from amaascore.assets.cfd import ContractForDifference
from amaascore.tools.csv_tools import objects_to_csv_stream

class CFDUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'CFDUploaderTest.csv'
        self.asset_id = 'GD1DISR12'

    def tearDown(self):
        pass

    def test_CFDUploadDownload(self):
        CFDUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile)
        CFDUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=[self.asset_id])

if __name__ == '__main__':
    unittest.main()