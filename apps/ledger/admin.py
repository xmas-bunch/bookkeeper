"""
Admin views configuration for ledger application.
"""
from django.contrib.admin import site, ModelAdmin, TabularInline

from .models import Transaction, Entry


class EntryInlineAdmin(TabularInline):
    """
    Inline admin for Entry model.
    """
    model = Entry


class TransactionAdmin(ModelAdmin):
    """
    Admin for Transaction model.
    """
    list_display = ('id', 'summary')
    inlines = (EntryInlineAdmin,)


site.register(Transaction, TransactionAdmin)
