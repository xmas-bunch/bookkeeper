"""
Admin view configuration for accounts application.
"""
from django.contrib.admin import site, ModelAdmin, TabularInline

from .models import Balance, Account


class BalanceInlineAdmin(TabularInline):
    """
    Inline admin for Balance model.
    """
    model = Balance


class AccountAdmin(ModelAdmin):
    """
    Admin for Account model.
    """
    list_display = ('id', 'name',)
    inlines = (BalanceInlineAdmin,)


site.register(Account, AccountAdmin)
