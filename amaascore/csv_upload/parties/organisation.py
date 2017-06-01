import logging.config
import csv

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaascore.parties.organisation import Organisation
from amaascore.parties.interface import PartiesInterface
from amaasutils.logging_utils import DEFAULT_LOGGING

class OrganisationUploader(object):

    def __init__(self):
        pass

    @staticmethod
    def json_handler(orderedDict, params):
        Dict = dict(orderedDict)
        for key, var in params.items():
            Dict[key]=var
        party_id = Dict.pop('party_id', None)
        party_status = Dict.pop('party_status', 'Active')
        org = Organisation(party_id=party_id, party_status=party_status, **dict(Dict))
        return org

    @staticmethod
    def upload(asset_manager_id, csvpath):
        """convert csv file rows to objects and insert;
           asset_manager_id from the UI (login)"""
        interface = PartiesInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params = {'asset_manager_id': asset_manager_id}
        with open(csvpath) as csvfile:
            orgs = csv_stream_to_objects(stream=csvfile, json_handler=OrganisationUploader.json_handler, **params)
        for org in orgs:
            interface.new(org)
            logger.info('Creating new book %s successfully', org.party_id)

    @staticmethod
    def download(asset_manager_id, party_id_list):
        """retrieve the organisations mainly for test purposes"""
        interface = PartiesInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        orgs = []
        for party_id in party_id_list:
            orgs.append(interface.retrieve(asset_manager_id=asset_manager_id, party_id=party_id))
            interface.deactivate(asset_manager_id=asset_manager_id, party_id=party_id)
        return orgs
        