import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.books.book import BookUploader
from amaascore.books.book import Book


class BookUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = 1
        self.csvfile = 'BookUploaderTest.csv'
        self.book_id = random_string(10)
        file_content = []
        line_to_override = {3:[self.book_id, 'Trading', 'Active', '123', '123', '', 'UTC', 'USD', '', '', '']}
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

    def test_BookUploadDownload(self):
        BookUploader().upload(asset_manager_id=self.asset_manager_id, csvpath=self.csvfile)
        BookUploader().download(asset_manager_id=self.asset_manager_id, book_id_list=[self.book_id])

if __name__ == '__main__':
    unittest.main()
