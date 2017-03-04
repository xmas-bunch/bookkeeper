"""
Models for accounts application.
"""
from django.db.models import Model, ForeignKey, CharField

from ..common.db.models import OwnedEntity


class Account(OwnedEntity):
    """
    Main account object, holding balances.
    """
    name = CharField(
        max_length=100,
        help_text="Descriptive title of the account."
    )


class Balance(Model):
    """
    Amount held in a given currency for an account, usually one per account
    but can be more than one in credits (cards).
    """
    account = ForeignKey(
        'Account'
    )
    currency = ForeignKey(
        'currencies.Currency'
    )
