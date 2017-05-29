import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.parties.organisation import OrganisationUploader
from amaascore.parties.organisation import Organisation
from amaascore.tools.csv_tools import objects_to_csv_stream

class OrganisationUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'OrganisationUploaderTest.csv'
        self.party_ids = []
        for i in range(2):
            self.party_ids.append(random_string(8))

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        for party_id in self.party_ids:
            OrganisationUploader().upload(asset_manager_id=self.asset_manager_id, csvpath=self.csvfile, party_id=party_id)
        OrganisationUploader().download(asset_manager_id=self.asset_manager_id, party_id_list=self.party_ids)

if __name__ == '__main__':
    unittest.main()