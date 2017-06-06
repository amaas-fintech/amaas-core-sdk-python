import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.asset_managers.asset_manager import AssetManagerUploader

class AssetManagerUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.asset_manager_ids = [random_string(8), random_string(8)]
        self.csvfile = 'AssetManagerUploaderTest.csv'
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow(['AssetManager', 'Bank', self.asset_manager_ids[0], 'Active', '123', 'Basic', '321', 'UTC', '5pm'])
            writer.writerow(['AssetManager', 'Bank', self.asset_manager_ids[1], 'Active', '123', 'Basic', '321', 'UTC', '5pm'])

    def tearDown(self):
        pass

    def test_AMUploadDownload(self):
        AssetManagerUploader().upload(csvpath=self.csvfile)
        AssetManagerUploader().download(asset_manager_id_list=self.asset_manager_ids)

if __name__ == '__main__':
    unittest.main()