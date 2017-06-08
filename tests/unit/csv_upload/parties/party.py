import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.data import Uploader

class PartyUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.party_ids = [random_string(8), random_string(8)]
        self.csvfile = 'PartyUploaderTest.csv'
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow(['Party', self.party_ids[0], 'Active', 'SGD', 'description',
                             '12345', 'Singapore', 'SGD', '123', '6789', 'true', '1', 'true', '2', 'false'])
            writer.writerow(['Party', self.party_ids[1], 'Active', 'SGD', 'description',
                             '12345', 'Singapore', 'SGD', '123', '6789', 'true', '1', 'true', '2', 'false'])

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        Uploader().upload(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id)
        Uploader().download(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id, data_id_type='party_id', data_id_list=self.party_ids)

if __name__ == '__main__':
    unittest.main()