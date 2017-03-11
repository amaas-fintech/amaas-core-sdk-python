import copy
import json
import unittest

from amaascore.core.reference import Reference
from amaascore.parties.individual import Individual
from amaascore.parties.party import Party
from amaascore.tools.generate_party import generate_individual


class IndividualTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure
        self.individual = generate_individual()  # Using a broker as an example company
        self.party_id = self.individual.party_id

    def tearDown(self):
        pass

    def test_Party(self):
        self.assertEqual(type(self.individual), Individual)
        self.assertTrue(isinstance(self.individual, Party))

if __name__ == '__main__':
    unittest.main()
