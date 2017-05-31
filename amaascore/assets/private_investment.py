from datetime import datetime, date
from dateutil import parser

from amaascore.assets.asset import Asset
from amaascore.assets.enums import PRIVATE_INVESTMENT_CATEGORY, PRIVATE_INVESTMENT_SHARE_TYPE, PRIVATE_INVESTMENT_SUBCATEGORY

class PrivateInvestment(Asset):

    def __init__(self, asset_manager_id, asset_id, client_id, asset_issuer_id=None, asset_status='Active',
                 display_name='', roll_price=True,
                 description='', country_id=None, venue_id=None, currency=None, additional=None,
                 comments=None, links=None, references=None,
                 category=None, sub_category=None, investment_date=None, value_date=None, num_shares=None,
                 price_share=None, share_class=None, series=None, share_type=None, coupon=None, coupon_freq=None,
                 upfront_fee=None, exit_fee=None, management_fee=None, performance_fee=None,
                 hurdle=None, margin=None, high_water_mark=None, maturity_date=None,
                 lock_up_period=None, investment_term=None,
                 *args, **kwargs):
        if not hasattr(self, 'asset_class'):  # A more specific child class may have already set this
            self.asset_class = 'PrivateInvestment'
        super(PrivateInvestment, self).__init__(asset_manager_id=asset_manager_id, asset_id=asset_id, fungible=False,
                                        asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                        display_name=display_name, roll_price=roll_price,
                                        description=description, country_id=country_id, venue_id=venue_id,
                                        currency=currency, comments=comments, links=links, references=references,
                                        client_id=client_id, additional=additional, *args, **kwargs)
        self.category = category
        self.sub_category = sub_category
        self.investment_date = investment_date
        self.value_date = value_date
        self.num_shares = num_shares
        self.price_share = price_share
        self.share_class = share_class
        self.series = series
        self.share_type = share_type
        self.coupon = coupon
        self.coupon_freq = coupon_freq
        self.upfront_fee = upfront_fee
        self.exit_fee = exit_fee
        self.management_fee = management_fee
        self.performance_fee = performance_fee
        self.hurdle = hurdle
        self.margin = margin
        self.high_water_mark = high_water_mark
        self.maturity_date = maturity_date
        self.lock_up_period = lock_up_period
        self.investment_date = investment_date
        self.investment_term = investment_term

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if category in PRIVATE_INVESTMENT_CATEGORY:
            self._category=category
        else:
            raise ValueError('Invalid input of category, please indicate Others if %s not in our list', category)

    @property
    def sub_category(self):
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        category = self._category
        if category in PRIVATE_INVESTMENT_SUBCATEGORY.keys():
            if sub_category in PRIVATE_INVESTMENT_SUBCATEGORY[category]:
                self._sub_category = sub_category
            else:
                raise ValueError('Invalid input of sub_category: %s', sub_category)
        else:
            raise ValueError('please set up category correctly')

    @property
    def investment_date(self):
        return self._investment_date

    @investment_date.setter
    def investment_date(self, investment_date):
        self._investment_date = investment_date

    @property
    def value_date(self):
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        self._value_date = value_date

    @property
    def num_shares(self):
        return self._num_shares

    @num_shares.setter
    def num_shares(self, num_shares):
        if isinstance(num_shares, int) or isinstance(num_shares, str):
            num_shares = int(float(num_shares))
            self._num_shares = num_shares
        else:
            raise ValueError("num_shares should be an integer :%s", num_shares)

    @property
    def price_share(self):
        return self._price_share

    @price_share.setter
    def price_share(self, price_share):
        if isinstance(price_share, float) or isinstance(price_share, int) or isinstance(price_share, str):
            price_share = float(price_share)
            self._price_share = price_share
        else:
            raise ValueError("Price per share must be a number :%s", price_share)

    @property
    def share_class(self):
        return self._share_class

    @share_class.setter
    def share_class(self, share_class):
        self._share_class = share_class

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, series):
        self._series = series

    @property
    def share_type(self):
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        if share_type in PRIVATE_INVESTMENT_SHARE_TYPE:
            self._share_type = share_type
        else:
            raise ValueError('Invalid input of share_type %s not in our list', share_type)

    @property
    def coupon(self):
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        self._coupon = coupon

    @property
    def coupon_freq(self):
        return self._coupon_freq

    @coupon_freq.setter
    def coupon_freq(self, coupon_freq):
        self._coupon_freq = coupon_freq

    @property
    def upfront_fee(self):
        return self._upfront_fee

    @upfront_fee.setter
    def upfront_fee(self, upfront_fee):
        self._upfront_fee = upfront_fee

    @property
    def exit_fee(self):
        return self._exit_fee

    @exit_fee.setter
    def exit_fee(self, exit_fee):
        self._exit_fee = exit_fee

    @property
    def management_fee(self):
        return self._management_fee

    @management_fee.setter
    def management_fee(self, management_fee):
        self._management_fee = management_fee

    @property
    def performance_fee(self):
        return self._performance_fee

    @performance_fee.setter
    def performance_fee(self, performance_fee):
        self._performance_fee = performance_fee

    @property
    def hurdle(self):
        return self._hurdle

    @hurdle.setter
    def hurdle(self, hurdle):
        self._hurdle = hurdle

    @property
    def margin(self):
        return self._margin

    @margin.setter
    def margin(self, margin):
        self._margin = margin

    @property
    def high_water_mark(self):
        return self._high_water_mark

    @high_water_mark.setter
    def high_water_mark(self, high_water_mark):
        self._high_water_mark = high_water_mark

    @property
    def maturity_date(self):
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        self._maturity_date = maturity_date

    @property
    def lock_up_period(self):
        return self._lock_up_period

    @lock_up_period.setter
    def lock_up_period(self, lock_up_period):
        try:
            lock_up_period = float(lock_up_period)
            self._lock_up_period = lock_up_period
        except Exception:
            raise ValueError('invalid input of lock up period %s, cannot be converted to floating number', lock_up_period)
    @property
    def investment_term(self):
        return self._investment_term

    @investment_term.setter
    def investment_term(self, investment_term):
        try:
            investment_term = float(investment_term)
            self._investment_term = investment_term
        except Exception:
            raise ValueError('invalid input of investment type %s, cannot be converted to floating number', investment_term)

