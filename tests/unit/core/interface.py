from __future__ import absolute_import, division, print_function, unicode_literals

from configparser import ConfigParser
import os.path
import tempfile
import unittest

from amaascore.core.interface import Interface
from amaascore.exceptions import AMaaSException


class InterfaceTest(unittest.TestCase):

    def test_NoAuth(self):
        interface = Interface(endpoint='DUMMY', use_auth=False)
        self.assertEqual(interface.auth_token, '')

    def test_GenerateConfigFilename(self):
        # This isn't a great test since there are too many permutations to properly test
        interface = Interface(endpoint='DUMMY')
        self.assertIsNotNone(interface.generate_config_filename())

    def test_ReadTokenWithPath(self):
        # Create a dummy file
        config = ConfigParser()
        config['auth'] = {'token': 'TEST_VALUE'}
        filename = os.path.join(tempfile.gettempdir(), 'amaas.cfg')
        # Writing our configuration file to 'example.cfg'
        with open(filename, 'w') as configfile:
            config.write(configfile)
        interface = Interface(endpoint='DUMMY', use_auth=True, config_filename=filename)
        self.assertEqual(interface.auth_token, 'TEST_VALUE')
        os.remove(filename)

    def test_ReadTokenMissingPath(self):
        with self.assertRaisesRegexp(AMaaSException, 'Invalid AMaaS config file'):
            interface = Interface(endpoint='DUMMY', use_auth=True, config_filename='INVALID')

if __name__ == '__main__':
    unittest.main()
