import datetime
import random
import unittest

from amaascore.transactions.transaction import Transaction
from amaascore.transactions.interface import TransactionsInterface
from amaascore.tools.generate_asset import generate_asset
from amaascore.tools.generate_transaction import generate_transaction


class TransactionsInterfaceTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.transactions_interface = TransactionsInterface()
        self.asset_manager_id = 1
        self.asset = generate_asset(asset_manager_id=self.asset_manager_id)
        self.transaction = generate_transaction(asset_manager_id=self.asset_manager_id, asset_id=self.asset.asset_id)
        self.transaction_id = self.transaction.transaction_id

    def tearDown(self):
        pass

    def create_transaction_asset(self):
        transaction_asset_fields = ['asset_manager_id', 'asset_id', 'asset_status', 'asset_class', 'asset_type',
                                    'primary_identifier', 'fungible', 'description']
        asset_json = self.asset.to_json()
        transaction_asset_json = {attr: asset_json.get(attr) for attr in transaction_asset_fields}
        transaction_asset_json['primary_identifier'] = 'TEST'  # This is temporary, we need to handle this better
        self.transactions_interface.upsert_transaction_asset(transaction_asset_json=transaction_asset_json)

    def test_New(self):
        self.create_transaction_asset()
        self.assertIsNone(self.transaction.created_time)
        transaction = self.transactions_interface.new(self.transaction)
        # TODO - this should be populated by the New call.
        #self.assertIsNotNone(transaction.created_time)
        self.assertEqual(transaction.transaction_id, self.transaction_id)

    def test_Amend(self):
        self.create_transaction_asset()
        transaction = self.transactions_interface.new(self.transaction)
        self.assertEqual(transaction.version, 1)
        new_settlement_date = transaction.settlement_date + datetime.timedelta(days=1)
        transaction.settlement_date = new_settlement_date
        transaction = self.transactions_interface.amend(transaction)
        self.assertEqual(transaction.settlement_date, new_settlement_date)
        self.assertEqual(transaction.version, 2)

    def test_Retrieve(self):
        self.create_transaction_asset()
        self.transactions_interface.new(self.transaction)
        transaction = self.transactions_interface.retrieve(self.transaction.asset_manager_id,
                                                           self.transaction.transaction_id)
        self.assertEqual(type(transaction), Transaction)

    def test_Cancel(self):
        self.create_transaction_asset()
        self.transactions_interface.new(self.transaction)
        self.transactions_interface.cancel(self.transaction.asset_manager_id, self.transaction.transaction_id)
        transaction = self.transactions_interface.retrieve(self.transaction.asset_manager_id,
                                                           self.transaction.transaction_id)
        self.assertEqual(transaction.transaction_id, self.transaction_id)
        self.assertEqual(transaction.transaction_status, 'Cancelled')

    def test_Search(self):
        all_transactions = self.transactions_interface.search()
        random_transaction_index = random.randint(0, len(all_transactions)-1)
        asset_manager_id = all_transactions[random_transaction_index].asset_manager_id
        asset_manager_transactions = [transaction for transaction in all_transactions
                                      if transaction.asset_manager_id == asset_manager_id]
        transactions = self.transactions_interface.search(asset_manager_ids=[asset_manager_id])
        self.assertEqual(len(transactions), len(asset_manager_transactions))

if __name__ == '__main__':
    unittest.main()
