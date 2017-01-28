#  All possible class names must be inserted into the globals collection.
#  If there is a better way of doing this, please suggest!
from amaascore.assets.asset import Asset
from amaascore.assets.bond import BondCorporate, BondGovernment, BondMortgage
from amaascore.assets.bond_option import BondOption
from amaascore.assets.currency import Currency
from amaascore.assets.derivative import Derivative
from amaascore.assets.equity import Equity
from amaascore.assets.foreign_exchange import ForeignExchange, NonDeliverableForward

import inspect


def json_to_asset(json_asset):
    clazz = globals().get(json_asset.get('asset_type'))
    args = inspect.getargspec(clazz.__init__)
    # is not None is important so it includes zeros and False
    constructor_dict = {arg: json_asset.get(arg) for arg in args.args
                        if json_asset.get(arg) is not None and arg != 'self'}
    # Some fields are always added in, even though they're not explicitly part of the constructor
    constructor_dict.update({attr: json_asset.get(attr) for attr in clazz.amaas_model_attributes()})
    return clazz(**constructor_dict)

