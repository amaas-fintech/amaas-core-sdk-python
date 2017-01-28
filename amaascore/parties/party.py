import copy
import re

from amaascore.error_messages import ERROR_LOOKUP
from amaascore.core.amaas_model import AMaaSModel


class Party(AMaaSModel):

    def __init__(self, asset_manager_id, party_id, party_status='Active', description='', addresses={}, emails={},
                 references={}, *args, **kwargs):
        self.asset_manager_id = asset_manager_id
        self.party_id = party_id
        self.party_status = party_status
        if not hasattr(self, 'party_class'):  # A more specific child class may have already set this
            self.party_class = 'Party'
        self.party_type = self.__class__.__name__
        self.description = description
        self.addresses = addresses
        self.emails = emails
        self.references = references
        super(Party, self).__init__(*args, **kwargs)

    def upsert_address(self, address_type, address):
        addresses = copy.deepcopy(self.addresses)
        addresses.update({address_type: address})
        self.addresses = addresses

    @property
    def addresses(self):
        if hasattr(self, '_addresses'):
            return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        if not isinstance(addresses, dict):
            raise ValueError(ERROR_LOOKUP.get('address_invalid') % (str(addresses), self.party_id,
                                                                    self.asset_manager_id))
        primary = [address.address_primary for address in addresses.values() if address.address_primary]
        # If addresses are present, one of them must be primary
        if len(addresses) and len(primary) != 1:
            raise ValueError(ERROR_LOOKUP.get('address_primary') % (self.party_id, self.asset_manager_id))
        self._addresses = addresses

    def upsert_email(self, email_type, email):
        emails = copy.deepcopy(self.emails)
        emails.update({email_type: email})
        self.emails = emails

    @property
    def emails(self):
        if hasattr(self, '_emails'):
            return self._emails

    @emails.setter
    def emails(self, emails):
        if not isinstance(emails, dict):
            raise ValueError(ERROR_LOOKUP.get('email_invalid') % (str(emails), self.party_id, self.asset_manager_id))
        primary = [email.email_primary for email in emails.values() if email.email_primary]
        # If emails are present, one of them must be primary
        if len(emails) and len(primary) != 1:
            raise ValueError(ERROR_LOOKUP.get('email_primary') % (self.party_id, self.asset_manager_id))
        # Validate email addresses
        invalid = [email.email for email in emails.values() if not re.match('[^@]+@[^@]+\.[^@]+', email.email)]
        if invalid:
            raise ValueError(ERROR_LOOKUP.get('email_address_invalid') % (str(invalid), self.party_id,
                                                                          self.asset_manager_id))
        self._emails = emails
