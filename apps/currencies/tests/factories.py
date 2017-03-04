"""
Factories for currencies unit tests.
"""
from factory import DjangoModelFactory

from ..models import Currency


class CurrencyFactory(DjangoModelFactory):
    """
    Factory for generic currency.
    """
    class Meta(object):
        model = Currency


class ARSFactory(CurrencyFactory):
    """
    Factory for AR Pesos.
    """
    name = 'Peso Argentino'
    code = 'ARS'
    symbol = 'AR$'


class USDFactory(CurrencyFactory):
    """
    Factory for US Dollars.
    """
    name = 'United States Dollar'
    code = 'USD'
    symbol = 'US$'
