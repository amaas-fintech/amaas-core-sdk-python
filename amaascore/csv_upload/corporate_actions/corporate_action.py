import logging.config
import csv

from amaascore.tools.csv_tools import csv_stream_to_objects

from amaascore.corporate_actions.corporate_action import CorporateAction
from amaascore.corporate_actions.dividend import Dividend
from amaascore.corporate_actions.notification import Notification
from amaascore.corporate_actions.split import Split 
from amaascore.corporate_actions.interface import CorporateActionsInterface

from amaasutils.logging_utils import DEFAULT_LOGGING

from amaascore.csv_upload.corporate_actions.utils import process_normal
from amaascore.csv_upload.corporate_actions.utils import Reference

class CorporateActionUploader(object):

    def __init__(self):
        pass

    @staticmethod
    def json_handler(orderedDict, params=dict()):
        Dict = dict(orderedDict)
        amaasclass = Dict.pop('amaasclass', '')
        for key, var in params.items():
            Dict[key] = var
        Dict = process_normal(Dict)
        clazz = globals()[amaasclass]
        asset_manager = clazz(**dict(Dict))
        return asset_manager

    @staticmethod
    def upload(csvpath, asset_manager_id):
        """convert csv file rows to objects and insert;
           asset_manager_id from the UI (login)"""
        interface = CorporateActionsInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        params={'asset_manager_id': asset_manager_id}
        with open(csvpath) as csvfile:
            actions = csv_stream_to_objects(stream=csvfile, json_handler=CorporateActionUploader.json_handler, params=params)
        for action in actions:
            interface.new(action)
            logger.info('Uploading new corporate_action %s successfully', action.asset_manager_id)

    @staticmethod
    def download(asset_manager_id, corporate_action_id_list):
        """retrieve the Asset Managers mainly for test purposes"""
        interface = CorporateActionsInterface()
        logging.config.dictConfig(DEFAULT_LOGGING)
        logger = logging.getLogger(__name__)
        actions = []
        for corporate_action_id in corporate_action_id_list:
            actions.append(interface.retrieve(asset_manager_id=asset_manager_id,corporate_action_id=corporate_action_id))
            interface.cancel(asset_manager_id=asset_manager_id,corporate_action_id=corporate_action_id)
        return actions

