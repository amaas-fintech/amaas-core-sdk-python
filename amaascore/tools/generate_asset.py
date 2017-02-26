import datetime
from decimal import Decimal
import random

from amaascore.assets.asset import Asset
from amaascore.assets.bond import BondGovernment
from amaascore.assets.bond_option import BondOption
from amaascore.assets.foreign_exchange import ForeignExchange
from amaascore.core.reference import Reference
from amaascore.tools.helpers import random_string

REFERENCE_TYPES = ['External']


def generate_common(asset_manager_id=None, asset_id=None):

    common = {'asset_manager_id': asset_manager_id or random.randint(1, 1000),
              'asset_id': asset_id or str(random.randint(1, 1000)),
              'currency': random.choice(['SGD', 'USD'])
              }

    return common


def generate_asset(asset_manager_id=None, asset_id=None):

    common = generate_common(asset_manager_id=asset_manager_id, asset_id=asset_id)
    common['fungible'] = random.choice([True, False])

    asset = Asset(**common)
    references = {ref_type: Reference(reference_value=random_string(10)) for ref_type in REFERENCE_TYPES}

    asset.references.update(references)
    return asset


def generate_bond(asset_manager_id=None, asset_id=None):
    props = generate_common(asset_manager_id=asset_manager_id, asset_id=asset_id)
    bond = BondGovernment(par=Decimal('1000'),
                          pay_frequency='M',  # Need to check how we want to represent this
                          coupon=Decimal('0.05'),
                          **props)
    return bond


def generate_bond_option(asset_manager_id=None, asset_id=None, put_call=None, strike=None):
    props = generate_common(asset_manager_id=asset_manager_id, asset_id=asset_id)
    asset = BondOption(put_call=put_call or random.choice(['Put', 'Call']),
                       strike=strike or Decimal(random.uniform(99.0, 102.0)).quantize(Decimal('0.01')),
                       **props)
    return asset


def generate_foreignexchange(asset_id=None):
    asset = ForeignExchange(asset_id=asset_id)
    return asset
