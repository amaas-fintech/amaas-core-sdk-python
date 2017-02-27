from datetime import date, datetime
from dateutil import parser
from decimal import Decimal

from amaascore.assets.derivative import Derivative
from amaascore.assets.option_mixin import OptionMixin


class BondOption(Derivative, OptionMixin):

    def __init__(self, asset_manager_id, put_call, strike, underlying_asset_id, option_type, asset_id=None,
                 asset_issuer_id=None, asset_status='Active', description='', country_id=None, venue_id=None,
                 issue_date=date.min, expiry_date=date.max, references={}, *args, **kwargs):
        self.put_call = put_call
        self.strike = strike
        self.underlying_asset_id = underlying_asset_id
        self.option_type = option_type
        super(BondOption, self).__init__(asset_manager_id=asset_manager_id, asset_id=asset_id,
                                         asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                         description=description, country_id=country_id, venue_id=venue_id,
                                         expiry_date=expiry_date, references=references,
                                         issue_date=issue_date, *args, **kwargs)
