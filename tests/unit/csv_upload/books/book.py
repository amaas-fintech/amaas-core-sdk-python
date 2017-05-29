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
        self.csvfile = 'BookUploaderTest.csv'
        self.book_ids = []
        for i in range(2):
            self.book_ids.append(random_string(8))

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        for book_id in self.book_ids:
            BookUploader().upload(asset_manager_id=self.asset_manager_id, csvpath=self.csvfile, book_id=book_id)
        BookUploader().download(asset_manager_id=self.asset_manager_id, book_id_list=self.book_ids)

if __name__ == '__main__':
    unittest.main()