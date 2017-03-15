from __future__ import absolute_import, division, print_function, unicode_literals

import os
import tempfile
import unittest

from amaascore.parties.party import Party
from amaascore.parties.utils import json_to_party, parties_to_csv, parties_to_csv_stream, csv_filename_to_parties, \
    csv_stream_to_parties
from amaascore.tools.generate_party import generate_party


class PartyUtilsTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True  # Print complete error message on failure

    def tearDown(self):
        pass

    def test_JsonToParty(self):
        party = generate_party()
        json_party = party.to_json()
        gen_party = json_to_party(json_party)
        self.assertEqual(gen_party, party)

    def test_PartiesToCSV(self):
        filename = tempfile.gettempdir() + '/test.csv'
        parties = [generate_party() for i in range(5)]
        parties_to_csv(parties=parties, filename=filename)
        # Read the file back out again
        with open(filename, 'r') as temp_file:
            data = temp_file.readlines()
        self.assertEqual(len(data), 6)  # 5 parties + header
        os.remove(filename)

    def test_PartiesToCSVStream(self):
        file_desc, temp_filepath = tempfile.mkstemp()
        parties = [generate_party() for i in range(5)]
        with open(temp_filepath, 'w') as temp_file:
            parties_to_csv_stream(parties=parties, stream=temp_file)
        # Read the file back out again
        with open(temp_filepath, 'r') as temp_file:
            data = temp_file.readlines()
        self.assertEqual(len(data), 6)  # 5 parties + header
        os.close(file_desc)
        os.remove(temp_filepath)

    def test_FilenameToParties(self):
        # Generate file
        filename = tempfile.gettempdir() + '/test.csv'
        parties = [generate_party() for i in range(5)]
        parties_to_csv(parties=parties, filename=filename)
        parties = csv_filename_to_parties(filename)
        self.assertEqual(len(parties), 5)
        self.assertEqual(type(parties[0]), Party)
        os.remove(filename)

    def test_StreamToParties(self):
        # Generate file
        filename = tempfile.gettempdir() + '/test.csv'
        parties = [generate_party() for i in range(5)]
        parties_to_csv(parties=parties, filename=filename)
        with open(filename, 'r') as stream:
            parties = csv_stream_to_parties(stream)
        self.assertEqual(len(parties), 5)
        self.assertEqual(type(parties[0]), Party)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
