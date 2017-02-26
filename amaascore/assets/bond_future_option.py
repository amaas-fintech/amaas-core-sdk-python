from decimal import Decimal

from amaascore.assets.future_option import FutureOption


class BondFutureOption(FutureOption):

    def __init__(self, asset_manager_id, asset_id, put_call, strike, underlying_asset_id, asset_issuer_id=None,
                 asset_status='Active', issue_date=None, expiry_date=None, description='', country_id=None,
                 venue_id=None, references={}, *args, **kwargs):
        super(BondFutureOption, self).__init__(asset_manager_id=asset_manager_id, asset_id=asset_id,
                                               asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                               description=description, country_id=country_id, venue_id=venue_id,
                                               references=references, issue_date=issue_date, expiry_date=expiry_date,
                                               put_call=put_call, strike=strike,
                                               underlying_asset_id=underlying_asset_id, *args, **kwargs)
