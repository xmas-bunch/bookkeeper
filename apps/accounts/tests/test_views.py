"""
Test cases for accounts views.
"""
import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Account
from .factories import AccountFactory, ARSBalanceFactory, USDBalanceFactory


class AccountsViewsTestCase(TestCase):
    """
    Tests for accounts views.

    So far, they are:
    * list_accounts
    """
    def test_list_accounts(self):
        # Resolve list_accounts url
        url = reverse('accounts-list')

        # There are no accounts yet
        self.assertEqual(Account.objects.count(), 0)

        # View list of accounts: nothing
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, {'count': 0, 'objects': []})

        # Add an account with two balances
        ac = AccountFactory.create()
        ARSBalanceFactory.create(account=ac, value=100.57)
        USDBalanceFactory.create(account=ac, value=8.45)

        # View list of accounts: one account with two balances
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(
            response_data,
            {
                'count': 1,
                'objects': [{
                    'name': ac.name,
                    'display': str(ac),
                    'balances': [
                        {'currency': 'ARS', 'value': '100.57', 'display': 'ARS 100.57'},
                        {'currency': 'USD', 'value': '8.45', 'display': 'USD 8.45'}
                    ]
                }]
            }
        )

        # Clean up (by removing account domain everything's removed in cascade)
        ac.domain.delete()
