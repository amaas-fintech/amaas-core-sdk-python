import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.assets.energy_future import EnergyFutureUploader
from amaascore.assets.energy_future import EnergyFuture
from amaascore.tools.csv_tools import objects_to_csv_stream

class EnergyFutureUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'EnergyFutureUploaderTest.csv'
        self.asset_ids = [random_string(8), random_string(8)]
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow([self.asset_ids[0], 'Cash', '123', '123', '123', '123', '123', '09/01/01', 
                            '09/01/01', 'SGD', 'mirror', '123', 'USA', '123'])
            writer.writerow([self.asset_ids[1], 'Cash', '123', '123', '123', '123', '123', '09/01/01', 
                            '09/01/01', 'SGD', 'mirror', '123', 'USA', '123'])

    def tearDown(self):
        pass

    def test_EnergyFutureUploadDownload(self):
        EnergyFutureUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile)
        EnergyFutureUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=self.asset_ids)

if __name__ == '__main__':
    unittest.main()