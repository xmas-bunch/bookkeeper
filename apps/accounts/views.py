"""
Resource handlers for accounts application.
"""
import json

from django.db.models import Sum
from django.http import HttpResponse

from .models import Account, Balance


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
        # Get the balance subtotals for the account
        balances_subtotals = Balance.objects.filter(
            account=account
        ).group_by(
            'currency'
        ).annotate(
            balance_subtotal=Sum('balance')
        )

        # Build balance data from subtotals
        balance_data = [
            {'currency': b.currency__symbol,
             'balance': b.balance_subtotal}
            for b in balances_subtotals
        ]

        # Append account data to result list
        data.append({
            'name': account.name,
            'balances': balance_data
        })

    # Serialize data as JSON string
    response_content = json.dumps(data)

    # Return response with content
    return HttpResponse(response_content)
