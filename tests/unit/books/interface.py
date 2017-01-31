import random
import unittest

from amaascore.books.interface import BooksInterface
from amaascore.tools.generate_book import generate_book


class BooksInterfaceTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.books_interface = BooksInterface()
        self.book = generate_book()
        self.book_id = self.book.book_id

    def tearDown(self):
        pass

    def test_New(self):
        self.assertIsNone(self.book.created_time)
        book = self.books_interface.new(self.book)
        # TODO - this should be populated by the New call.
        #self.assertIsNotNone(book.created_time)
        self.assertEqual(book.book_id, self.book_id)

    def test_Amend(self):
        book = self.books_interface.new(self.book)
        self.assertEqual(book.version, 1)
        book.owner_id = 'TEST'
        book = self.books_interface.amend(book)
        self.assertEqual(book.owner_id, 'TEST')
        self.assertEqual(book.version, 2)

    def test_Retrieve(self):
        self.books_interface.new(self.book)
        book = self.books_interface.retrieve(self.book.asset_manager_id, self.book.book_id)
        self.assertEqual(book.book_id, self.book_id)

    def test_Retire(self):
        self.books_interface.new(self.book)
        self.books_interface.retire(self.book.asset_manager_id, self.book.book_id)
        book = self.books_interface.retrieve(self.book.asset_manager_id, self.book.book_id)
        self.assertEqual(book.book_id, self.book_id)
        self.assertEqual(book.book_status, 'Retired')

    def test_Search(self):
        all_books = self.books_interface.search()
        random_book_index = random.randint(0, len(all_books)-1)
        asset_manager_id = all_books[random_book_index].asset_manager_id
        asset_manager_books = [book for book in all_books if book.asset_manager_id == asset_manager_id]
        books = self.books_interface.search(asset_manager_ids=[asset_manager_id])
        self.assertEqual(len(books), len(asset_manager_books))

    def test_BooksByAssetManager(self):
        all_books = self.books_interface.search()
        random_book_index = random.randint(0, len(all_books)-1)
        asset_manager_id = all_books[random_book_index].asset_manager_id
        asset_manager_books = [book for book in all_books if book.asset_manager_id == asset_manager_id]
        books = self.books_interface.books_by_asset_manager(asset_manager_id=asset_manager_id)
        self.assertEqual(len(books), len(asset_manager_books))

if __name__ == '__main__':
    unittest.main()
