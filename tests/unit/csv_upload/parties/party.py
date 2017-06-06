import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.parties.party import PartyUploader

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
                             '{address_1:{line_one:12345,city:Singapore,country_id:SGD,address_primary:123,line_two:6789,active:true}}',
                             '{comment_1:{comment_value:1,active:true},comment_2:{comment_value:2,active:false}}',
                             '{email_1:{email:1@1.com,email_primary:true,active:true},email_2:{email:2@2.com,email_primary:false}}',
                             '{link_1:[{linked_party_id:12345},{linked_party_id:54321,active:true}],link_2:[{linked_party_id:12365}]}',
                             '{reference_1:{reference_value:1,active:true},reference_2:{reference_value:2}}'])
            writer.writerow(['Party', self.party_ids[1], 'Active', 'SGD', 'description',
                             '{address_1:{line_one:12345,city:Singapore,country_id:SGD,address_primary:123,line_two:6789,active:true}}',
                             '{comment_1:{comment_value:1,active:true},comment_2:{comment_value:2,active:false}}',
                             '{email_1:{email:1@1.com,email_primary:true,active:true},email_2:{email:2@2.com,email_primary:false}}',
                             '{link_1:[{linked_party_id:12345},{linked_party_id:54321,active:true}],link_2:[{linked_party_id:12365}]}',
                             '{reference_1:{reference_value:1,active:true},reference_2:{reference_value:2}}'])

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        PartyUploader().upload(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id)
        PartyUploader().download(asset_manager_id=self.asset_manager_id, party_id_list=self.party_ids)

if __name__ == '__main__':
    unittest.main()