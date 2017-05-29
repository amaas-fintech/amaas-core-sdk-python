import logging.config
import csv

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaascore.assets.automobile import Automobile
from amaascore.assets.interface import AssetsInterface
from amaasutils.logging_utils import DEFAULT_LOGGING

class AutomobileUploader(object):

    def __init__(self):
        pass

    @staticmethod
    def json_handler(orderedDict, params):
        Dict = dict(orderedDict)
        for key, var in params.items():
            Dict[key]=var
        Dict.pop('asset_id', None)
        asset_id = params.pop('asset_id', None)
        asset_status = Dict.pop('asset_status','Active')
        trans_type = Dict.pop('trans_type', 0)
        automobile = Automobile(asset_id=asset_id, asset_status=asset_status, **dict(Dict))
        return automobile

    @staticmethod
    def upload(asset_manager_id, client_id, csvpath, asset_id):
        """convert csv file rows to objects and insert;
           asset_manager_id and client_id from the UI (login)"""
        interface = AssetsInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params = {'asset_manager_id': asset_manager_id, 'client_id': client_id, 'asset_id': asset_id}
        with open(csvpath) as csvfile:
            automobiles = csv_stream_to_objects(stream=csvfile, json_handler=AutomobileUploader.json_handler, **params)
        for automobile in automobiles:
            interface.new(automobile)
            logger.info('Creating new equity %s successfully', automobile.display_name)

    @staticmethod
    def download(asset_manager_id, asset_id_list):
        """retrieve the assets mainly for test purposes"""
        interface = AssetsInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        automobiles = []
        for asset_id in asset_id_list:
            automobiles.append(interface.retrieve(asset_manager_id=asset_manager_id, asset_id=asset_id))
            interface.deactivate(asset_manager_id=asset_manager_id, asset_id=asset_id)
        return automobiles