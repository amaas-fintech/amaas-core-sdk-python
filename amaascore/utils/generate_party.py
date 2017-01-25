import random

from amaascore.core.reference import Reference
from amaascore.parties.party import Party
from amaascore.parties.party_children import Address, Email
from amaascore.utils.helpers import random_string


def generate_common(asset_manager_id=None, party_id=None, party_class=None):
    common = {'asset_manager_id': asset_manager_id or random.randint(1, 1000),
              'party_id': party_id or str(random.randint(1, 1000)),
              'party_class': party_class or 'Party'
              }

    return common


def generate_party(asset_manager_id=None, party_id=None):
    references = {'PartyDB': Reference(random_string(10))}
    attributes = generate_common(asset_manager_id=asset_manager_id, party_id=party_id)
    party = Party(**attributes)
    # Does this screw up the party due to mutability concerns?  Do some testing.
    party.references.update(references)
    party.upsert_address('Registered', generate_address(address_primary=True))
    party.upsert_email('Office', generate_email(email_primary=True))
    return party


def generate_address(country_id=None, address_primary=None):
    address = Address(line_one=random_string(20),
                      line_two=random.choice([None, random_string(10)]),
                      city=random_string(10),
                      region=random_string(10),
                      postal_code=random_string(6),
                      country_id=country_id or random_string(3),  # Make this a real country code
                      address_primary=address_primary or False)
    return address


def generate_email(email=None, email_primary=None):
    return Email(email=email or (random_string(10) + '@amaas.com'), email_primary=email_primary or False)
