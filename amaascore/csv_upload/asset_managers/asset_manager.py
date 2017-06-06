import logging.config
import csv

from amaascore.tools.csv_tools import csv_stream_to_objects
from amaascore.asset_managers.asset_manager import AssetManager
from amaascore.asset_managers.relationship import Relationship
from amaascore.asset_managers.interface import AssetManagersInterface
from amaasutils.logging_utils import DEFAULT_LOGGING

class AssetManagerUploader(object):

    def __init__(self):
        pass

    @staticmethod
    def json_handler(orderedDict, params=dict()):
        Dict = dict(orderedDict)
        amaasclass = Dict.pop('amaasclass', '')
        for key, var in params.items():
            Dict[key]=var
        clazz = globals()[amaasclass]
        asset_manager = clazz(**dict(Dict))
        return asset_manager

    @staticmethod
    def upload(csvpath):
        """convert csv file rows to objects and insert;
           asset_manager_id from the UI (login)"""
        interface = AssetManagersInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params=dict()
        with open(csvpath) as csvfile:
            managers = csv_stream_to_objects(stream=csvfile, json_handler=AssetManagerUploader.json_handler, params=params)
        print(managers)
        for manager in managers:
            interface.new(manager)
            logger.info('Uploading new asset_manager %s successfully', manager.asset_manager_id)

    @staticmethod
    def download(asset_manager_id_list):
        """retrieve the Asset Managers mainly for test purposes"""
        interface = AssetManagersInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        managers = []
        for asset_manager_id in asset_manager_id_list:
            managers.append(interface.retrieve(asset_manager_id=asset_manager_id))
            interface.deactivate(asset_manager_id=asset_manager_id)
        return managers

