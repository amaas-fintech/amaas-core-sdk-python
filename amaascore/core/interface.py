from __future__ import absolute_import, division, print_function, unicode_literals

import requests

class Interface(object):
    """
    Currently this class doesn't do anything - but I anticipate it will be needed in the future.
    """

    def __init__(self, endpoint):
        # Add authentication routine here
        self.auth_token = ''
        self.endpoint = endpoint
        self.session = requests.Session()
        self.session.headers.update({'Authorization': self.auth_token})
