import requests

from amaascore.transactions.utils import json_to_transaction
from amaascore.core.interface import Interface
from config import ENDPOINTS


class TransactionsInterface(Interface):

    def __init__(self):
        endpoint = ENDPOINTS.get('transactions')
        super(TransactionsInterface, self).__init__(endpoint=endpoint)

    def new(self, transaction):
        url = self.endpoint + '/transactions'
        response = requests.post(url, json=transaction.to_interface())
        if response.ok:
            transaction = json_to_transaction(response.json())
            return transaction
        else:
            print "HANDLE THIS PROPERLY"
            print response.content

    def amend(self, transaction):
        url = '%s/transactions/%s/%s' % (self.endpoint, transaction.asset_manager_id, transaction.transaction_id)
        response = requests.put(url, json=transaction.to_interface())
        if response.ok:
            transaction = json_to_transaction(response.json())
            return transaction
        else:
            print "HANDLE THIS PROPERLY"
            print response.content

    def retrieve(self, asset_manager_id, transaction_id):
        url = '%s/transactions/%s/%s' % (self.endpoint, asset_manager_id, transaction_id)
        response = requests.get(url)
        if response.ok:
            return json_to_transaction(response.json())
        else:
            print "HANDLE THIS PROPERLY"
            print response.content

    def cancel(self, asset_manager_id, transaction_id):
        url = '%s/transactions/%s/%s' % (self.endpoint, asset_manager_id, transaction_id)
        response = requests.delete(url)
        if response.ok:
            print "DO SOMETHING?"
        else:
            print "HANDLE THIS PROPERLY"
            print response.content

    def search(self, asset_manager_ids=None, transaction_ids=None):
        search_params = {}
        # Potentially roll this into a loop through args rather than explicitly named - depends on additional validation
        if asset_manager_ids:
            search_params['asset_manager_ids'] = asset_manager_ids
        if transaction_ids:
            search_params['transaction_ids'] = transaction_ids
        url = self.endpoint + '/transactions'
        response = requests.get(url, params=search_params)
        if response.ok:
            transactions = []
            for json_transaction in response.json():
                transaction = json_to_transaction(json_transaction)
                transactions.append(transaction)
            return transactions
        else:
            print "HANDLE THIS PROPERLY"
            print response.content

    def upsert_transaction_asset(self, transaction_asset_json):
        """
        This API should not be called in normal circumstances as the asset cache will populate itself from the assets
        which are created via the Assets API.  However, it can be useful for certain testing scenarios.
        :param transaction_asset_json:
        :return:
        """
        url = self.endpoint + '/assets'
        response = requests.post(url, json=transaction_asset_json)
        if response.ok:
            print "DO SOMETHING?"
        else:
            print "HANDLE THIS PROPERLY"
            print response.content
