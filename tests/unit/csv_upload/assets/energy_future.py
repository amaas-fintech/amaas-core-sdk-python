import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.assets.energy_future import EnergyFutureUploader
from amaascore.assets.energy_future import EnergyFuture
from amaascore.tools.csv_tools import objects_to_csv_stream

class EnergyFutureUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.csvfile = 'EnergyFutureUploaderTest.csv'
        self.asset_id = 'GDHDISR12'

    def tearDown(self):
        pass

    def test_WarrantUploadDownload(self):
        EnergyFutureUploader().upload(asset_manager_id=self.asset_manager_id, client_id=self.client_id, csvpath=self.csvfile)
        EnergyFutureUploader().download(asset_manager_id=self.asset_manager_id, asset_id_list=[self.asset_id])

if __name__ == '__main__':
    unittest.main()