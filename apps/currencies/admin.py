"""
Admin views configuration for currencies application.
"""
from django.contrib.admin import site, ModelAdmin

from .models import Currency, ExchangeRate


class CurrencyAdmin(ModelAdmin):
    """
    Admin for Currency model.
    """
    list_display = ('id', 'code', 'symbol', 'name',)


class ExchangeRateAdmin(ModelAdmin):
    """
    Admin for ExchangeRate model.
    """
    list_display = ('bought_currency', 'sold_currency', 'value')


site.register(Currency, CurrencyAdmin)
site.register(ExchangeRate, ExchangeRateAdmin)
