import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.books.book import BookUploader
from amaascore.books.book import Book
from amaascore.tools.csv_tools import objects_to_csv_stream

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
            writer.writerow([self.book_ids[0], '', 'Active', '', '', '', '', 'SGD', '', '', ''])
            writer.writerow([self.book_ids[1], '', 'Active', '', '', '', '', 'SGD', '', '', ''])

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        BookUploader().upload(asset_manager_id=self.asset_manager_id, csvpath=self.csvfile)
        BookUploader().download(asset_manager_id=self.asset_manager_id, book_id_list=self.book_ids)

if __name__ == '__main__':
    unittest.main()