import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.parties.party import PartyUploader
from amaascore.parties.party import Party
from amaascore.tools.csv_tools import objects_to_csv_stream

class PartyUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'PartyUploaderTest.csv'
        self.party_ids = []
        for i in range(2):
            self.party_ids.append(random_string(8))

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        for party_id in self.party_ids:
            PartyUploader().upload(asset_manager_id=self.asset_manager_id, csvpath=self.csvfile, party_id=party_id)
        PartyUploader().download(asset_manager_id=self.asset_manager_id, party_id_list=self.party_ids)

if __name__ == '__main__':
    unittest.main()