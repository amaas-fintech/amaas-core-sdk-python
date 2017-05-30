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
        self.party_ids = [random_string(8), random_string(8)]
        self.csvfile = 'OrganisationUploaderTest.csv'
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow([self.party_ids[0], 'Active', 'SGD', '', '', '', ''])
            writer.writerow([self.party_ids[1], 'Active', 'SGD', '', '', '', ''])

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        OrganisationUploader().upload(asset_manager_id=self.asset_manager_id, csvpath=self.csvfile)
        OrganisationUploader().download(asset_manager_id=self.asset_manager_id, party_id_list=self.party_ids)

if __name__ == '__main__':
    unittest.main()