import logging.config
import csv

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaascore.books.book import Book
from amaascore.books.interface import BooksInterface
from amaasutils.logging_utils import DEFAULT_LOGGING

class BookUploader(object):

    def __init__(self):
        pass

    @staticmethod
    def json_handler(orderedDict, params):
        Dict = dict(orderedDict)
        for key, var in params.items():
            Dict[key]=var
        book_id = Dict.pop('book_id', None)
        book_status = Dict.pop('book_status', 'Active')
        book_type = Dict.pop('book_type', 'Trading')
        book = Book(book_id=book_id, book_status=book_status, **dict(Dict))
        return book

    @staticmethod
    def upload(asset_manager_id, csvpath):
        """convert csv file rows to objects and insert;
           asset_manager_id from the UI (login)"""
        interface = BooksInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params = {'asset_manager_id': asset_manager_id}
        with open(csvpath) as csvfile:
            books = csv_stream_to_objects(stream=csvfile, json_handler=BookUploader.json_handler, **params)
        for book in books:
            interface.new(book)
            logger.info('Creating new book %s successfully', book.book_id)

    @staticmethod
    def download(asset_manager_id, book_id_list):
        """retrieve the books mainly for test purposes"""
        interface = BooksInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        books = []
        for book_id in book_id_list:
            books.append(interface.retrieve(asset_manager_id=asset_manager_id, book_id=book_id))
            interface.retire(asset_manager_id=asset_manager_id, book_id=book_id)
        return books

