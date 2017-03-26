from __future__ import absolute_import, division, print_function, unicode_literals

from decimal import Decimal
import unittest

from amaascore.assets.future import Future
from amaascore.tools.generate_asset import generate_future


class FutureTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.future = generate_future()
        self.asset_id = self.future.asset_id

    def tearDown(self):
        pass

    def test_Future(self):
        self.assertEqual(type(self.future), Future)

if __name__ == '__main__':
    unittest.main()
