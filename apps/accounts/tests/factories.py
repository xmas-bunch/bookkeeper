"""
Factories for accounts unit tests.
"""
from factory import DjangoModelFactory, Faker, SubFactory

from ...common.tests.factories import GroupFactory
from ...currencies.tests.factories import ARSFactory, USDFactory
from ..models import Account, Balance


class AccountFactory(DjangoModelFactory):
    """
    Factory for generic account.
    """
    class Meta(object):
        model = Account

    domain = SubFactory(GroupFactory)
    name = Faker('sentence', nb_words=3)


class BalanceFactory(DjangoModelFactory):
    """
    Factory for generic currency balance.
    """
    class Meta(object):
        model = Balance

    account = SubFactory(AccountFactory)
    value = Faker('random_number', digits=2)


class ARSBalanceFactory(BalanceFactory):
    """
    Factory for balance in ARS.
    """
    currency = SubFactory(ARSFactory)


class USDBalanceFactory(BalanceFactory):
    """
    Factory for balance in USD.
    """
    currency = SubFactory(USDFactory)
