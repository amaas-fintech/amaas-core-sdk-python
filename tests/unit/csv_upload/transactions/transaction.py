import unittest
import csv
import random

from amaasutils.random_utils import random_string
from amaascore.csv_upload.transactions.transaction import TransactionUploader

class TransactionUploaderTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.asset_manager_id = self.client_id = 1
        self.transaction_ids = [random_string(8), random_string(8)]
        self.csvfile = 'TransactionUploaderTest.csv'
        with open(self.csvfile, 'r+', newline='') as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                header = row
                break
        with open(self.csvfile, 'w+', newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(header)
            writer.writerow(['Transaction', self.transaction_ids[0], '1', '2', 'Buy', '3', '10', '09/01/01', '09/01/01', '1', 'SGD', 'USD', 'DSC', '09/01/01', 'Allocation', 'New',
                             '{charge_1:{charge_value:10,currency:SGD,active:true},charge_2:{charge_value:1,currency:SGD}}'
                             '{code_1:{code_value:1,active:true},code_2:{code_value:2}}'
                             '{comment_1:{comment_value:1,active:true},comment_2:{comment_value:2}}'
                             '{link_1:[{linked_transaction_id:12345},{linked_transaction_id:54321,active:true}],link_2:[{linked_transaction_id:12365}]}'
                             '{party_1:{party_id:1,active:true},party_2:{party_id:2,active:false}}'
                             '{{reference_value:1,active:true},{reference_value:2}}'])
            writer.writerow(['Transaction', self.transaction_ids[1], '1', '2', 'Buy', '3', '10', '09/01/01', '09/01/01', '1', 'SGD', 'USD', 'DSC', '09/01/01', 'Allocation', 'New',
                             '{charge_1:{charge_value:10,currency:SGD,active:true},charge_2:{charge_value:1,currency:SGD}}'
                             '{code_1:{code_value:1,active:true},code_2:{code_value:2}}'
                             '{comment_1:{comment_value:1,active:true},comment_2:{comment_value:2}}'
                             '{link_1:[{linked_transaction_id:12345},{linked_transaction_id:54321,active:true}],link_2:[{linked_transaction_id:12365}]}'
                             '{party_1:{party_id:1,active:true},party_2:{party_id:2,active:false}}'
                             '{{reference_value:1,active:true},{reference_value:2}}'])

    def tearDown(self):
        pass

    def test_PartyUploadDownload(self):
        TransactionUploader().upload(csvpath=self.csvfile, asset_manager_id=self.asset_manager_id)
        TransactionUploader().download(asset_manager_id=self.asset_manager_id, transaction_id_list=self.transaction_ids)

if __name__ == '__main__':
    unittest.main()