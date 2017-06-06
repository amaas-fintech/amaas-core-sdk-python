import logging.config
import csv
import json

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaasutils.logging_utils import DEFAULT_LOGGING

from amaascore.transactions.position import Position
from amaascore.transactions.transaction import Transaction

from amaascore.transactions.children import Charge, Code, Comment, Link, Party, Reference
from amaascore.csv_upload.transactions.utils import process_normal

from amaascore.transactions.interface import TransactionsInterface

class TransactionUploader(object):

    def __init__(self):
        pass

    @staticmethod
    def json_handler(orderedDict, params=dict()):
        Dict = dict(orderedDict)
        for key, var in params.items():
            Dict[key]=var
        data_class = Dict.pop('amaasclass', None)
        Dict = process_normal(Dict)
        #construct the class using Dict as params argument
        obj = globals()[data_class](**dict(Dict))
        return obj

    @staticmethod
    def upload(csvpath, asset_manager_id=None):
        """convert csv file rows to transactions and insert;
           asset_manager_id and possibly client_id from the UI (login)"""
        interface = TransactionsInterface(environment='local')
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params = {'asset_manager_id': asset_manager_id}
        with open(csvpath) as csvfile:
            transactions = csv_stream_to_objects(stream=csvfile, json_handler=TransactionUploader.json_handler, params=params)
        for transaction in transactions:
            interface.new(transaction)
            logger.info('Creating this transaction and upload to database successfully')

    @staticmethod
    def download(asset_manager_id, transaction_id_list):
        """retrieve the transactions mainly for test purposes"""
        interface = TransactionsInterface(environment='local')
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        transactions = []
        for transaction_id in transaction_id_list:
            transactions.append(interface.retrieve(asset_manager_id=asset_manager_id, transaction_id=transaction_id))
        return transactions
