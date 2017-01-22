from datetime import date, datetime
from dateutil import parser
from decimal import Decimal

from amaascore.assets.derivative import Derivative
from amaascore.assets.option import OptionMixin


class BondOption(Derivative, OptionMixin):

    def __init__(self, asset_manager_id, asset_id=None, maturity_date=None, coupon=None, par=None,
                 asset_issuer_id=None, asset_status='Active', description='', country_id=None, venue_id=None,
                 client_id=None, issue_date=None, references={}, *args, **kwargs):
        self.asset_manager_id = asset_manager_id
        super(BondOption, self).__init__(asset_manager_id=self.asset_manager_id, asset_id=asset_id,
                                         asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                         description=description, country_id=country_id, venue_id=venue_id,
                                         maturity_date=maturity_date, references=references, client_id=client_id,
                                         coupon=coupon, par=par, issue_date=issue_date, *args, **kwargs)
