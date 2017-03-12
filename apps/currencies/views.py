"""
Request handlers for currencies application.
"""
from django.http import JsonResponse

from .models import Currency


def list_currencies(request):
    """
    Get a list of all the currencies available.

    :param request: WSGI request
    :return: JSONResponse with list of currencies
    """
    # Build all data at once using list comprehension
    data = [
        {'name': currency.name,
         'code': currency.code,
         'symbol': currency.symbol}
        for currency in Currency.objects.all()
    ]

    # Return json response with data
    return JsonResponse({'count': len(data), 'objects': data})

