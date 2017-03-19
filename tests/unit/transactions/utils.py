from __future__ import absolute_import, division, print_function, unicode_literals

import os
import os.path
import tempfile
import unittest

from amaascore.transactions.position import Position
from amaascore.transactions.transaction import Transaction
from amaascore.transactions.utils import json_to_transaction, json_to_position, transactions_to_csv, \
    transactions_to_csv_stream, csv_filename_to_transactions, csv_stream_to_transactions
from amaascore.tools.generate_transaction import generate_transaction, generate_position


class TransactionUtilsTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure

    def tearDown(self):
        pass

    def test_JsonToTransaction(self):
        transaction = generate_transaction()
        json_transaction = transaction.to_json()
        gen_transaction = json_to_transaction(json_transaction)
        self.assertEqual(gen_transaction, transaction)

    def test_JsonToPosition(self):
        position = generate_position()
        json_position = position.to_json()
        gen_position = json_to_position(json_position)
        self.assertEqual(gen_position, position)

    def test_TransactionsToCSV(self):
        filename = os.path.join(tempfile.gettempdir(), 'test.csv')
        transactions = [generate_transaction() for i in range(5)]
        transactions_to_csv(transactions=transactions, filename=filename)
        # Read the file back out again
        with open(filename, 'r') as temp_file:
            data = temp_file.readlines()
        self.assertEqual(len(data), 6)  # 5 transactions + header
        os.remove(filename)

    def test_TransactionsToCSVStream(self):
        file_desc, temp_filepath = tempfile.mkstemp()
        transactions = [generate_transaction() for i in range(5)]
        with open(temp_filepath, 'w') as temp_file:
            transactions_to_csv_stream(transactions=transactions, stream=temp_file)
        # Read the file back out again
        with open(temp_filepath, 'r') as temp_file:
            data = temp_file.readlines()
        self.assertEqual(len(data), 6)  # 5 transactions + header
        os.close(file_desc)
        os.remove(temp_filepath)

    def test_FilenameToTransactions(self):
        # Generate file
        filename = os.path.join(tempfile.gettempdir(), 'test.csv')
        transactions = [generate_transaction() for i in range(5)]
        transactions_to_csv(transactions=transactions, filename=filename)
        transactions = csv_filename_to_transactions(filename)
        self.assertEqual(len(transactions), 5)
        self.assertEqual(type(transactions[0]), Transaction)
        os.remove(filename)

    def test_StreamToTransactions(self):
        # Generate file
        filename = os.path.join(tempfile.gettempdir(), 'test.csv')
        transactions = [generate_transaction() for i in range(5)]
        transactions_to_csv(transactions=transactions, filename=filename)
        with open(filename, 'r') as stream:
            transactions = csv_stream_to_transactions(stream)
        self.assertEqual(len(transactions), 5)
        self.assertEqual(type(transactions[0]), Transaction)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
