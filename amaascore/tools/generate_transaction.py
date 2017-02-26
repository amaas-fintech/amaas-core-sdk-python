import datetime
from decimal import Decimal
import random

from amaascore.core.reference import Reference
from amaascore.transactions.position import Position
from amaascore.transactions.transaction import Transaction
from amaascore.transactions.children import Charge, Code, Comment, Link, Party
from amaascore.tools.helpers import random_string

CHARGE_TYPES = ['Tax', 'Commission']
CODE_TYPES = ['Settle Code', 'Client Classifier']
COMMENT_TYPES = ['Trader']
PARTY_TYPES = ['Prime Broker']
REFERENCE_TYPES = ['External']


def generate_common(asset_manager_id=None, asset_book_id=None, counterparty_book_id=None, asset_id=None, quantity=None,
                    price=None, transaction_date=None, transaction_id=None):

    # Explicitly handle price is None (in case price is 0)
    price = Decimal(random.uniform(1.0, 1000.0)).quantize(Decimal('0.01')) if price is None else price

    common = {'asset_manager_id': asset_manager_id or random.randint(1, 1000),
              'asset_book_id': asset_book_id or random_string(8),
              'counterparty_book_id': counterparty_book_id or random_string(8),
              'asset_id': asset_id or str(random.randint(1, 1000)),
              'quantity': quantity or Decimal(random.randint(-5000, 5000)),
              'price': price,
              'transaction_date': transaction_date or datetime.date.today(),
              'transaction_currency': random.choice(['SGD', 'USD']),
              'settlement_currency': random.choice(['SGD', 'USD']),
              'transaction_id': transaction_id
              }

    common['settlement_date'] = (datetime.timedelta(days=2) + common['transaction_date'])

    if quantity >= 0:
        common['transaction_action'] = random.choice(['Buy', 'Receive'])
    else:
        common['transaction_action'] = random.choice(['Sell', 'Short Sell', 'Transfer'])
    return common


def generate_transaction(asset_manager_id=None, asset_book_id=None, counterparty_book_id=None,
                         asset_id=None, quantity=None, transaction_date=None, transaction_id=None,
                         price=None, net_affecting_charges=None):

    common = generate_common(asset_manager_id=asset_manager_id, asset_book_id=asset_book_id,
                             counterparty_book_id=counterparty_book_id, asset_id=asset_id, quantity=quantity,
                             price=price, transaction_date=transaction_date, transaction_id=transaction_id)

    transaction = Transaction(**common)
    charges = {charge_type: Charge(charge_value=Decimal(random.uniform(1.0, 100.0)).quantize(Decimal('0.01')),
                                   currency=random.choice(['USD', 'SGD']),
                                   net_affecting=net_affecting_charges or random.choice([True, False]))
               for charge_type in CHARGE_TYPES}

    links = {'Single': Link(linked_transaction_id=random_string(8)),
             'Multiple': [Link(linked_transaction_id=random_string(8)) for x in range(3)]}

    codes = {code_type: Code(code_value=random_string(8)) for code_type in CODE_TYPES}
    comments = {comment_type: Comment(comment_value=random_string(8)) for comment_type in COMMENT_TYPES}
    parties = {party_type: Party(party_id=random_string(8)) for party_type in PARTY_TYPES}
    references = {ref_type: Reference(reference_value=random_string(10)) for ref_type in REFERENCE_TYPES}

    transaction.charges.update(charges)
    transaction.codes.update(codes)
    transaction.comments.update(comments)
    transaction.links.update(links)
    transaction.parties.update(parties)
    transaction.references.update(references)
    return transaction


def generate_position(asset_manager_id=None, asset_book_id=None, asset_id=None, quantity=None):
    position = Position(asset_manager_id=asset_manager_id or random.randint(1, 1000),
                        asset_book_id=asset_book_id or random_string(8),
                        asset_id=asset_id or str(random.randint(1, 1000)),
                        quantity=quantity or Decimal(random.randint(1, 50000)))
    return position