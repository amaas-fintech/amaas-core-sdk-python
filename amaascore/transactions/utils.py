from amaascore.transactions.position import Position
from amaascore.transactions.transaction import Transaction


def json_to_position(json_position):
    position = Position(**json_position)
    return position


def json_to_transaction(json_transaction):
    for (collection_name, clazz) in Transaction.children().items():
        children = json_transaction.pop(collection_name, {})
        collection = {}
        for (child_type, child_json) in children.items():
            child = clazz(**child_json)
            collection[child_type] = child
        json_transaction[collection_name] = collection
    transaction = Transaction(**json_transaction)
    return transaction


def json_to_party(json_to_convert):
    # Iterate through the party children, converting the various JSON attributes into the relevant class type

    clazz = globals().get(json_to_convert.get('party_type'))
    party = clazz(**json_to_convert)
    return party

