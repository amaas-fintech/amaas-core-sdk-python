import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.assets.equity import EquityUploader
from amaascore.assets.equity import Equity
from amaascore.tools.csv_tools import objects_to_csv_stream

class EquityUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        #self.EquityUploader = EquityUploader()
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'EquityUploaderTest.csv'
        self.asset_id = random_string(10)
        print(self.asset_id)
        file_content = []
        line_to_override = {2:[self.asset_id, '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '', '']}
        with open(self.csvfile) as csv_read:
            csvreader = csv.reader(csv_read)
            file_content.extend(csvreader)
        with open(self.csvfile, 'w+') as csv_write:
            csvwriter = csv.writer(csv_write)
            for line, row in enumerate(file_content):
                data = line_to_override.get(line, row)
                csvwriter.writerow(data)

    def tearDown(self):
        pass

    def test_EquityUploadDownload(self):
        EquityUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile)
        EquityUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=[self.asset_id])

if __name__ == '__main__':
    unittest.main()
