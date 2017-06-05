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
from amaascore.parties.interface import PartiesInterface
from amaasutils.logging_utils import DEFAULT_LOGGING

class PartyUploader(object):

    def __init__(self):
        pass

    @staticmethod
    def json_handler(orderedDict, params):
        Dict = dict(orderedDict)
        for key, var in params.items():
            Dict[key]=var
        party_id = Dict.pop('party_id', None)
        party_status = Dict.pop('party_status', 'Active')
        party_class = Dict.pop('amaasparty', 'Party')
        party = globals()[party_class](party_id=party_id, party_status=party_status, **dict(Dict))
        return party

    @staticmethod
    def upload(asset_manager_id, csvpath):
        """convert csv file rows to objects and insert;
           asset_manager_id from the UI (login)"""
        interface = PartiesInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params = {'asset_manager_id': asset_manager_id}
        with open(csvpath) as csvfile:
            parties = csv_stream_to_objects(stream=csvfile, json_handler=PartyUploader.json_handler, **params)
        for party in parties:
            interface.new(party)
            logger.info('Creating new book %s successfully', party.party_id)

    @staticmethod
    def download(asset_manager_id, party_id_list):
        """retrieve the parties mainly for test purposes"""
        interface = PartiesInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        parties = []
        for party_id in party_id_list:
            parties.append(interface.retrieve(asset_manager_id=asset_manager_id, party_id=party_id))
            interface.deactivate(asset_manager_id=asset_manager_id, party_id=party_id)
        return parties
        