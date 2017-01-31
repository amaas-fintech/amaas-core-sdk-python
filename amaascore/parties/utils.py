#  All possible class names must be inserted into the globals collection.
#  If there is a better way of doing this, please suggest!
from amaascore.parties.broker import Broker
from amaascore.parties.company import Company
from amaascore.parties.exchange import Exchange
from amaascore.parties.fund import Fund
from amaascore.parties.government_agency import GovernmentAgency
from amaascore.parties.individual import Individual
from amaascore.parties.organisation import Organisation
from amaascore.parties.party import Party


def json_to_party(json_to_convert):
    # Iterate through the party children, converting the various JSON attributes into the relevant class type
    for (collection_name, clazz) in Party.children().items():
        children = json_to_convert.pop(collection_name, {})
        collection = {}
        for (child_type, child_json) in children.items():
            child = clazz(**child_json)
            collection[child_type] = child
        json_to_convert[collection_name] = collection
    clazz = globals().get(json_to_convert.get('party_type'))
    party = clazz(**json_to_convert)
    return party

