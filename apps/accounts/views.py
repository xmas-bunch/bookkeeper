"""
Resource handlers for accounts application.
"""
from django.http import JsonResponse

from .models import Account


def list_accounts(request):
    """
    Handler to return a list of accounts as JSON data.

    :param request: request sent by dispatcher
    :return: rendered data
    """
    # Start with empty list
    data = []

    # Build data for every account
    for account in Account.objects.all():
        # Build balance data for account
        balance_data = [
            {'currency': b.currency.symbol,
             'value': b.value}
            for b in account.balances.all()
        ]

        # Append account data to result list
        data.append({
            'name': account.name,
            'balances': balance_data
        })

    # Return JSON response with data
    return JsonResponse({'count': len(data), 'objects': data})
