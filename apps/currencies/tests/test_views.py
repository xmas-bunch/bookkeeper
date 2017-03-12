"""
Test cases for currencies views.
"""
import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Currency
from .factories import USDFactory, ARSFactory


class CurrenciesViewsTestCase(TestCase):
    """
    Tests for currencies views.

    So far, they are:
    * list_currencies
    """
    def test_list_currencies(self):
        # Resolve list_accounts url
        url = reverse('currencies-list')

        # There are no accounts yet
        self.assertEqual(Currency.objects.count(), 0)

        # View list of accounts: nothing
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, {'count': 0, 'objects': []})

        # Add two currencies
        USDFactory.create()
        ARSFactory.create()

        # View list of currencies: both returned
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(
            response_data,
            {
                'count': 2,
                'objects': [
                    {'name': c.name,
                     'short_name': str(c),
                     'symbol': c.symbol,
                     'code': c.code}
                    for c in Currency.objects.all()
                ]
            }
        )

        # Clean up
        Currency.objects.all().delete()
