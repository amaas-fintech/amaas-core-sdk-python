# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

from amaasutils.logging_utils import DEFAULT_LOGGING
from datetime import date
import random
import unittest

from amaascore.market_data.interface import MarketDataInterface
from amaascore.tools.generate_market_data import generate_eod_price, generate_fx_rate

import logging.config
logging.config.dictConfig(DEFAULT_LOGGING)


class MarketDataInterfaceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
        cls.interface = MarketDataInterface()

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.maxDiff = None  # Print the complete diff message
        self.asset_manager_id = random.randint(1, 2**31-1)
        self.eod_price1 = generate_eod_price(asset_manager_id=self.asset_manager_id)
        self.eod_price2 = generate_eod_price(asset_manager_id=self.asset_manager_id)
        self.fx_rate1 = generate_fx_rate(asset_manager_id=self.asset_manager_id, asset_id='USDJPY')
        self.fx_rate2 = generate_fx_rate(asset_manager_id=self.asset_manager_id, asset_id='USDSGD')
        self.business_date = date.today()

    def tearDown(self):
        pass

    def test_PersistEODPrices(self):
        eod_prices = self.interface.persist_eod_prices(asset_manager_id=self.asset_manager_id,
                                                       business_date=self.business_date,
                                                       eod_prices=[self.eod_price1, self.eod_price2],
                                                       update_existing_prices=True)
        self.assertEqual(eod_prices, [self.eod_price1, self.eod_price2])

    def test_RetrieveEODPrices(self):
        self.interface.persist_eod_prices(asset_manager_id=self.asset_manager_id, business_date=self.business_date,
                                          eod_prices=[self.eod_price1, self.eod_price2],
                                          update_existing_prices=True)
        eod_prices = self.interface.retrieve_eod_prices(asset_manager_id=self.asset_manager_id,
                                                        business_date=self.business_date)
        self.assertEqual(set(eod_prices), {self.eod_price1, self.eod_price2})

    def test_RetrieveSpecificEODPrices(self):
        self.interface.persist_eod_prices(asset_manager_id=self.asset_manager_id, business_date=self.business_date,
                                          eod_prices=[self.eod_price1, self.eod_price2],
                                          update_existing_prices=True)
        eod_prices = self.interface.retrieve_eod_prices(asset_manager_id=self.asset_manager_id,
                                                        business_date=self.business_date,
                                                        asset_ids=[self.eod_price1.asset_id, self.eod_price2.asset_id])
        self.assertEqual(set(eod_prices), {self.eod_price1, self.eod_price2})

    def test_PersistFXRates(self):
        fx_rates = self.interface.persist_fx_rates(asset_manager_id=self.asset_manager_id,
                                                   business_date=self.business_date,
                                                   fx_rates=[self.fx_rate1, self.fx_rate2],
                                                   update_existing_rates=True)
        self.assertEqual(set(fx_rates), {self.fx_rate1, self.fx_rate2})

    def test_RetrieveFXRates(self):
        self.interface.persist_fx_rates(asset_manager_id=self.asset_manager_id, business_date=self.business_date,
                                        fx_rates=[self.fx_rate1, self.fx_rate2],
                                        update_existing_rates=True)
        fx_rates = self.interface.retrieve_fx_rates(asset_manager_id=self.asset_manager_id,
                                                    business_date=self.business_date)
        self.assertEqual(set(fx_rates), {self.fx_rate1, self.fx_rate2})

    def test_RetrieveSpecificFXRates(self):
        self.interface.persist_fx_rates(asset_manager_id=self.asset_manager_id, business_date=self.business_date,
                                        fx_rates=[self.fx_rate1, self.fx_rate2],
                                        update_existing_rates=True)
        fx_rates = self.interface.retrieve_fx_rates(asset_manager_id=self.asset_manager_id,
                                                    business_date=self.business_date,
                                                    asset_ids=[self.fx_rate1.asset_id, self.fx_rate2.asset_id])
        self.assertEqual(set(fx_rates), {self.fx_rate1, self.fx_rate2})

if __name__ == '__main__':
    unittest.main()
