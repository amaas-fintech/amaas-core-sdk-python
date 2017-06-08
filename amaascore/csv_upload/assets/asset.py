import logging.config
import csv
import json

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaasutils.logging_utils import DEFAULT_LOGGING

from amaascore.assets.asset import Asset
from amaascore.assets.automobile import Automobile
from amaascore.assets.bond import BondCorporate, BondGovernment, BondMortgage
from amaascore.assets.bond_future import BondFuture
from amaascore.assets.bond_future_option import BondFutureOption
from amaascore.assets.bond_option import BondOption
from amaascore.assets.cfd import ContractForDifference
from amaascore.assets.currency import Currency
from amaascore.assets.custom_asset import CustomAsset
from amaascore.assets.derivative import Derivative
from amaascore.assets.energy_future import EnergyFuture
from amaascore.assets.equity import Equity
from amaascore.assets.equity_future import EquityFuture
from amaascore.assets.etf import ExchangeTradedFund
from amaascore.assets.foreign_exchange import ForeignExchange, NonDeliverableForward
from amaascore.assets.fund import Fund
from amaascore.assets.future import Future
from amaascore.assets.future_option import FutureOption
from amaascore.assets.fx_option import ForeignExchangeOption
from amaascore.assets.index import Index
from amaascore.assets.index_future import IndexFuture
from amaascore.assets.interest_rate_future import InterestRateFuture
from amaascore.assets.listed_cfd import ListedContractForDifference
from amaascore.assets.listed_derivative import ListedDerivative
from amaascore.assets.option_mixin import OptionMixin
from amaascore.assets.real_asset import RealAsset
from amaascore.assets.real_estate import RealEstate
from amaascore.assets.sukuk import Sukuk
from amaascore.assets.synthetic import Synthetic
from amaascore.assets.synthetic_from_book import SyntheticFromBook
from amaascore.assets.synthetic_multi_leg import SyntheticMultiLeg
from amaascore.assets.wine import Wine
from amaascore.assets.warrants import Warrant

from amaascore.assets.children import Link, Reference
from amaascore.csv_upload.assets.utils import process_normal

from amaascore.assets.interface import AssetsInterface

class AssetUploader(object):

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
    def upload(csvpath, asset_manager_id=None, client_id=None):
        """convert csv file rows to assets and insert;
           asset_manager_id and possibly client_id from the UI (login)"""
        interface = AssetsInterface(environment='local')
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params = {'asset_manager_id': asset_manager_id, 'client_id': client_id}
        with open(csvpath) as csvfile:
            assets = csv_stream_to_objects(stream=csvfile, json_handler=AssetUploader.json_handler, params=params)
        for asset in assets:
            interface.new(asset)
            logger.info('Creating this asset and upload to database successfully')

    @staticmethod
    def download(asset_manager_id, asset_id_list):
        """retrieve the assets mainly for test purposes"""
        interface = AssetsInterface(environment='local')
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        assets = []
        for asset_id in asset_id_list:
            assets.append(interface.retrieve(asset_manager_id=asset_manager_id, asset_id=asset_id))
            #interface.deactivate(asset_manager_id=asset_manager_id, **Dict)
        return assets