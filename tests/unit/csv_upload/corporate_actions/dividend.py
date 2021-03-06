import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload import Uploader

class DividendUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.corporate_action_ids = [random_string(8), random_string(8)]
        self.csvfile = 'DividendUploaderTest.csv'
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow(['Dividend', self.corporate_action_ids[0], '09/01/01', '0.1', '1', 'Open', '1', '2', '09/01/01', '09/01/01', '1', '', ''])
            writer.writerow(['Dividend', self.corporate_action_ids[1], '09/01/01', '0.1', '1', 'Open', '1', '2', '09/01/01', '09/01/01', '1', '', ''])

    def tearDown(self):
        pass

    def test_DividendUploadDownload(self):
        Uploader().upload(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id)
        Uploader().download(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id, data_id_type='corporate_action_id', data_id_list=self.corporate_action_ids)

if __name__ == '__main__':
    unittest.main()