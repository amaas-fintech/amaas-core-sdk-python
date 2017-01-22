from decimal import Decimal

from amaascore.core.amaas_model import AMaaSModel


class Position(AMaaSModel):

    def __init__(self, asset_manager_id, asset_id, quantity, version=1, *args, **kwargs):

        self.asset_manager_id = asset_manager_id
        self.asset_id = asset_id
        self.quantity = quantity
        self.version = version
        super(Position, self).__init__(*args, **kwargs)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """
        Force the quantity to always be a decimal
        :param value:
        :return:
        """
        self._quantity = Decimal(value)