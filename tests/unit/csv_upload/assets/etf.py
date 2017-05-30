import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.assets.etf import ETFUploader
from amaascore.assets.etf import ExchangeTradedFund
from amaascore.tools.csv_tools import objects_to_csv_stream

class ETFUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'ETFUploaderTest.csv'
        self.asset_ids = [random_string(8), random_string(8)]
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow([self.asset_ids[0], '123', '123', '123', '123', 'Active', '123', '123', '123', 'USA', '123', 'USD', '09/01/01'])
            writer.writerow([self.asset_ids[1], '123', '123', '123', '123', 'Active', '123', '123', '123', 'USA', '123', 'USD', '09/01/01'])

    def tearDown(self):
        pass

    def test_ETFUploadDownload(self):
        ETFUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile)
        ETFUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=self.asset_ids)

if __name__ == '__main__':
    unittest.main()