import logging.config
import csv

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaascore.parties.broker import Broker
from amaascore.parties.company import Company
from amaascore.parties.exchange import Exchange
from amaascore.parties.fund import Fund
from amaascore.parties.government_agency import GovernmentAgency
from amaascore.parties.individual import Individual
from amaascore.parties.organisation import Organisation
from amaascore.parties.party import Party
from amaascore.parties.sub_fund import SubFund

from amaasutils.logging_utils import DEFAULT_LOGGING

from amaascore.parties.children import Link, Address, Email, Reference
from amaascore.csv_upload.parties.utils import process_normal

from amaascore.parties.interface import PartiesInterface

class PartyUploader(object):

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
        """convert csv file rows to parties and insert;
           asset_manager_id and possibly client_id from the UI (login)"""
        interface = PartiesInterface(environment='local')
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params = {'asset_manager_id': asset_manager_id, 'client_id': client_id}
        with open(csvpath) as csvfile:
            parties = csv_stream_to_objects(stream=csvfile, json_handler=PartyUploader.json_handler, params=params)
        for party in parties:
            interface.new(party)
            logger.info('Creating this party and upload to database successfully')

    @staticmethod
    def download(asset_manager_id, party_id_list):
        """retrieve the parties mainly for test purposes"""
        interface = PartiesInterface(environment='local')
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        parties = []
        for party_id in party_id_list:
            parties.append(interface.retrieve(asset_manager_id=asset_manager_id, party_id=party_id))
            #interface.deactivate(asset_manager_id=asset_manager_id, **Dict)
        return parties
        