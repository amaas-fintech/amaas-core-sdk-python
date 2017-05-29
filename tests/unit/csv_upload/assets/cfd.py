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
        #self.asset_id = 'GD1DISR12'
        self.asset_ids = []
        for i in range(2):
            self.asset_ids.append(random_string(8))

    def tearDown(self):
        pass

    def test_CFDUploadDownload(self):
        for asset_id in self.asset_ids:
            CFDUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile, asset_id=asset_id)
        CFDUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=self.asset_ids)

if __name__ == '__main__':
    unittest.main()