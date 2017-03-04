"""
Models for accounts application.
"""
from django.db.models import Model, ForeignKey, CharField

from ..common.db.models import OwnedEntity
from ..common.db.query import GroupByQuerySet


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
    # Custom manager to allow group_by method
    manager = GroupByQuerySet.as_manager()

    account = ForeignKey(
        'Account'
    )
    currency = ForeignKey(
        'currencies.Currency'
    )
