import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.corporate_actions.corporate_action import CorporateActionUploader

class CorporateActionUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.corporate_action_ids = [random_string(8), random_string(8)]
        self.csvfile = 'CorporateActionUploaderTest.csv'
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow(['CorporateAction', self.corporate_action_ids[0], '09/01/01', 'Open', '1', '1', '09/01/01', '09/01/01', '1', '', ''])
            writer.writerow(['CorporateAction', self.corporate_action_ids[1], '09/01/01', 'Open', '1', '1', '09/01/01', '09/01/01', '1', '', ''])

    def tearDown(self):
        pass

    def test_CorporateActionUploadDownload(self):
        CorporateActionUploader().upload(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id)
        CorporateActionUploader().download(asset_manager_id=self.asset_manager_id, corporate_action_id_list=self.corporate_action_ids)

if __name__ == '__main__':
    unittest.main()