import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.data import Uploader

class TransactionUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.transaction_ids = [random_string(8), random_string(8)]
        self.csvfile = 'TransactionUploaderTest.csv'
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow(['Transaction', self.transaction_ids[0], '1', '2', 'Buy', '3', '10', '09/01/01', '09/01/01', '1', 'SGD', 'USD', 'DSC', '09/01/01', 'Allocation', 'New'])
            writer.writerow(['Transaction', self.transaction_ids[1], '1', '2', 'Buy', '3', '10', '09/01/01', '09/01/01', '1', 'SGD', 'USD', 'DSC', '09/01/01', 'Allocation', 'New'])

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        Uploader().upload(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id)
        Uploader().download(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id, data_id_type='transaction_id', data_id_list=self.transaction_ids)

if __name__ == '__main__':
    unittest.main()