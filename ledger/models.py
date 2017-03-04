"""
Models for ledger application.
"""
from django.db.models import CharField, DecimalField, ForeignKey, Model, TextField

from ..common.db.models import OwnedEntity


class Transaction(OwnedEntity):
    """
    Multiple operation involving two or more entries into different accounts
    or with different currencies.
    """
    summary = CharField(
        max_length=100,
        help_text='Short description of the operation.'
    )
    description = TextField(
        help_text='Detailed description of the operation.'
    )


class Entry(Model):
    """
    Single operation on one account with one currency.
    """
    transaction = ForeignKey(
        'Transaction',
        related_name='entries'
    )
    account = ForeignKey(
        'accounts.Account'
    )
    concept = CharField(
        max_length=1,
        choices=(
            ('C', 'Credit'),
            ('D', 'Debit')
        )
    )
    currency = ForeignKey(
        'currencies.Currency'
    )
    value = DecimalField()
