from datetime import date
from decimal import Decimal

from amaascore.core.amaas_model import AMaaSModel


class EODPrice(AMaaSModel):

    def __init__(self, asset_manager_id, asset_id, eod_date, price):
        """

        :param asset_manager_id:
        :param asset_id:
        :param eod_date:
        :param price:
        """
        self.asset_manager_id = asset_manager_id
        self.asset_id = asset_id
        self.price = price
        self.eod_date = eod_date  # The date for which this is the EOD price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        """
        Force the price to always be a decimal
        :param value:
        :return:
        """
        if value is not None:
            self._price = Decimal(value)
