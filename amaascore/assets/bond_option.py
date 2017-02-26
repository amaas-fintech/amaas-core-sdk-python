from datetime import date, datetime
from dateutil import parser
from decimal import Decimal

from amaascore.assets.derivative import Derivative


class BondOption(Derivative):

    def __init__(self, asset_manager_id, put_call, strike, underlying_asset_id, asset_id=None, asset_issuer_id=None,
                 asset_status='Active', description='', country_id=None, venue_id=None, issue_date=None,
                 expiry_date=None, references={}, *args, **kwargs):
        self.put_call = put_call
        self.strike = strike
        self.underlying_asset_id = underlying_asset_id
        super(BondOption, self).__init__(asset_manager_id=asset_manager_id, asset_id=asset_id,
                                         asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                         description=description, country_id=country_id, venue_id=venue_id,
                                         expiry_date=expiry_date, references=references,
                                         issue_date=issue_date, *args, **kwargs)

    @property
    def put_call(self):
        if hasattr(self, '_put_call'):
            return self._put_call

    @put_call.setter
    def put_call(self, put_call):
        if put_call:
            if put_call in ['Put', 'Call']:
                self._put_call = put_call
            else:
                raise ValueError("Invalid value for put_call: %s" % put_call)

    @property
    def strike(self):
        if hasattr(self, '_strike'):
            return self._strike

    @strike.setter
    def strike(self, strike):
        """ Force strike to be a Decimal. """
        if strike:
            self._strike = Decimal(strike)