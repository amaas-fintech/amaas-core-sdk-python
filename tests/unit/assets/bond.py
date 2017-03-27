from __future__ import absolute_import, division, print_function, unicode_literals

from decimal import Decimal
import unittest

from amaascore.assets.bond import BondGovernment
from amaascore.tools.generate_asset import generate_bond


class BondTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.bond = generate_bond()
        self.asset_id = self.bond.asset_id

    def tearDown(self):
        pass

    def test_Bond(self):
        self.assertEqual(type(self.bond), BondGovernment)

if __name__ == '__main__':
    unittest.main()
