import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload import Uploader

class AutomobileUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'AutomobileUploaderTest.csv'
        self.asset_ids = [random_string(8), random_string(8)]
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow(['Automobile', self.asset_ids[0], '123', 'USA', '123', '123', '123', '01/05/09', '01/05/09', 'USD',
                             'Active', '01/05/09', '0', '1900', '01/05/09', '123', '123', '123', 'McLaren', 'amaas_super_car',
                             'White', 'R', 'M', 'super rare', 'DC', '1', 'GBR', '123', '123', 'LHD', '', '', '', '', '', '', '', '', '',
                             '12345', '54321', 'true', '1', 'true', '2'])
            writer.writerow(['Automobile', self.asset_ids[1], '123', 'USA', '123', '123', '123', '01/05/09', '01/05/09', 'USD',
                             'Active', '01/05/09', '0', '1900', '01/05/09', '123', '123', '123', 'McLaren', 'amaas_super_car',
                             'White', 'R', 'M', 'super rare', 'DC', '1', 'GBR', '123', '123', 'LHD', '', '', '', '', '', '', '', '', '',
                             '12345', '54321', 'true', '1', 'true', '2'])
    def tearDown(self):
        pass

    def test_AutomobileUploadDownload(self):
        Uploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile)
        Uploader().download(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id, data_id_type='asset_id', data_id_list=self.asset_ids)

if __name__ == '__main__':
    unittest.main()