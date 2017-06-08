import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.data import Uploader

class BookUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.book_ids = [random_string(8), random_string(8)]
        self.csvfile = 'BookUploaderTest.csv'
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow(['Book', self.book_ids[0], 'Counterparty', 'Active', '', '', '', '', 'SGD', '', '', ''])
            writer.writerow(['Book', self.book_ids[1], 'Counterparty', 'Active', '', '', '', '', 'SGD', '', '', ''])

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        Uploader().upload(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id)
        Uploader().download(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id, data_id_type='book_id', data_id_list=self.book_ids)

if __name__ == '__main__':
    unittest.main()