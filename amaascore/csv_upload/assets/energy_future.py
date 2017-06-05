import logging.config
import csv

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaascore.assets.energy_future import EnergyFuture
from amaascore.assets.interface import AssetsInterface
from amaasutils.logging_utils import DEFAULT_LOGGING

class EnergyFutureUploader(object):

    def __init__(self):
        pass

    @staticmethod
    def json_handler(orderedDict, params):
        Dict = dict(orderedDict)
        for key, var in params.items():
            Dict[key]=var
        asset_id = Dict.pop('asset_id', None)
        asset_status = Dict.pop('Active', None)
        energy_future = EnergyFuture(asset_id=asset_id, asset_status=asset_status, **dict(Dict))
        return energy_future

    @staticmethod
    def upload(asset_manager_id, client_id, csvpath):
        """convert csv file rows to objects and insert;
           asset_manager_id and client_id from the UI (login)"""
        interface = AssetsInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params = {'asset_manager_id': asset_manager_id, 'client_id': client_id}
        with open(csvpath) as csvfile:
            energy_futures = csv_stream_to_objects(stream=csvfile, json_handler=EnergyFutureUploader.json_handler, **params)
        for energy_future in energy_futures:
            interface.new(energy_future)
            logger.info('Creating new equity %s successfully', energy_future.display_name)

    @staticmethod
    def download(asset_manager_id, asset_id_list):
        """retrieve the assets mainly for test purposes"""
        interface = AssetsInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        energy_futures = []
        for asset_id in asset_id_list:
            energy_futures.append(interface.retrieve(asset_manager_id=asset_manager_id, asset_id=asset_id))
            interface.deactivate(asset_manager_id=asset_manager_id, asset_id=asset_id)
        return energy_futures

