from decimal import Decimal

from amaascore.assets.listed_derivative import ListedDerivative
from amaascore.assets.option_mixin import OptionMixin


class FutureOption(ListedDerivative, OptionMixin):

    def __init__(self, asset_manager_id, asset_id, put_call, strike, underlying_asset_id, option_type,
                 asset_issuer_id=None, asset_status='Active', issue_date=None, expiry_date=None, description='',
                 country_id=None, venue_id=None, references={}, *args, **kwargs):
        self.put_call = put_call
        self.strike = strike
        self.underlying_asset_id = underlying_asset_id
        self.option_type = option_type
        super(FutureOption, self).__init__(asset_manager_id=asset_manager_id, asset_id=asset_id,
                                           asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                           description=description, country_id=country_id, venue_id=venue_id,
                                           references=references, issue_date=issue_date, expiry_date=expiry_date,
                                           *args, **kwargs)
