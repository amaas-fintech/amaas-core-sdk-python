import csv

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaasutils.logging_utils import DEFAULT_LOGGING

from amaascore.assets.interface import AssetsInterface
from amaascore.parties.interface import PartiesInterface
from amaascore.books.interface import BooksInterface
from amaascore.corporate_actions.interface import CorporateActionsInterface

ASSET = ['Asset', 'Automobile', 'BondFutureOption', 'BondFuture', 'BondOption', 'Bond', 'ContractForDifference', 'Currency', 'CustomAsset', 
         'Derivative', 'EnergyFuture', 'EquityFuture', 'Equity', 'ExchangeTradedFund', 'ForeignExchange', 'Fund', 'FutureOption', 'Future'
         'ForeignExchangeOption', 'IndexFuture', 'Index', 'InterestRateFuture', 'ListedContractForDifference', 'ListedDerivative'
         'OptionMixin', 'RealAsset', 'RealEstate', 'Sukuk', 'SyntheticFromBook', 'SyntheticMultiLeg', 'Synthetic', 'Warrant', 'Wine']
PARTY = ['Broker', 'Company', 'Exchange', 'Fund', 'GovernmentAgency', 'Individual', 'Organisation', 'Party', 'SubFund']
BOOK = ['Book']
CORPORATE_ACTION = ['CorporateAction', 'Dividend', 'Notification', 'Split']

def interface_direct (csvpath):
    with open(csvpath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_class = row.get('amaasclass')
            break
    if data_class in ASSET:
        interface = AssetsInterface()
    elif data_class in PARTY:
        interface = PartiesInterface()
    elif data_class in BOOK:
        interface = BooksInterface()
    else:
        interface = CorporateActionsInterface()
    return interface