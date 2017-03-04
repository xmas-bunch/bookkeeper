"""
Models for accounts application.
"""
from django.db.models import CharField, DecimalField, ForeignKey, Model

from ..common.db.models import OwnedEntity
from ..common.db.query import GroupByQuerySet


class Account(OwnedEntity):
    """
    Main account object, holding balances.
    """
    # Database fields
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
    objects = GroupByQuerySet.as_manager()

    # Database fields
    account = ForeignKey(
        'Account',
        related_name='balances'
    )
    currency = ForeignKey(
        'currencies.Currency'
    )
    value = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
