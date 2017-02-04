#  All possible class names must be inserted into the globals collection.
#  If there is a better way of doing this, please suggest!
from amaascore.assets.asset import Asset
from amaascore.assets.bond import BondCorporate, BondGovernment, BondMortgage
from amaascore.assets.bond_option import BondOption
from amaascore.assets.currency import Currency
from amaascore.assets.derivative import Derivative
from amaascore.assets.equity import Equity
from amaascore.assets.foreign_exchange import ForeignExchange, NonDeliverableForward


def json_to_asset(json_asset):
    # Iterate through the asset children, converting the various JSON attributes into the relevant class type
    for (collection_name, clazz) in Asset.children().items():
        children = json_asset.pop(collection_name, {})
        collection = {}
        for (child_type, child_json) in children.items():
            child = clazz(**child_json)
            collection[child_type] = child
        json_asset[collection_name] = collection
    clazz = globals().get(json_asset.get('asset_type'))
    asset = clazz(**json_asset)
    return asset
