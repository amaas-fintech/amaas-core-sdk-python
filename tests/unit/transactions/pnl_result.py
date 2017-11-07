from __future__ import absolute_import, division, print_function, unicode_literals
from decimal import Decimal
import json
import unittest

from amaascore.transactions.pnl_result import PNLResult
from amaascore.tools.generate_transaction import generate_pnl_result


class PNLResultTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.pnl_result = generate_pnl_result()

    def tearDown(self):
        pass

    def test_PNLResult(self):
        self.assertEqual(type(self.pnl_result), PNLResult)

    def test_PNLPeriodEnum(self):
        with self.assertRaisesRegexp(ValueError, 'Unrecognized PnL period'):
            self.pnl_result.period = 'year to date'

    def test_PNLResultToDict(self):
        pnl_result_dict = self.pnl_result.to_dict()
        self.assertEqual(type(pnl_result_dict), dict)
        self.assertEqual(pnl_result_dict.get('total_pnl'), self.pnl_result.total_pnl)

    def test_PNLResultToJSON(self):
        pnl_result_json = self.pnl_result.to_json()
        self.assertEqual(Decimal(pnl_result_json.get('total_pnl')), self.pnl_result.total_pnl)
        json_total_pnl = Decimal(json.loads(json.dumps(pnl_result_json, ensure_ascii=False)).get('total_pnl'))
        self.assertEqual(json_total_pnl, self.pnl_result.total_pnl)


if __name__ == '__main__':
    unittest.main()
