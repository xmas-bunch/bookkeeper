"""
Models for currencies application.
"""
from django.db.models import CharField, DecimalField, ForeignKey, Model


class Currency(Model):
    """
    Currency object.
    """
    class Meta(object):
        verbose_name_plural = 'currencies'

    # Database fields
    name = CharField(
        max_length=100,
        help_text='Official name in home language.'
    )
    code = CharField(
        max_length=3,
        help_text='International, three-letter code.'
    )
    symbol = CharField(
        max_length=3,
        help_text='Short-hand symbol.'
    )

    def __str__(self):
        return self.code


class ExchangeRate(Model):
    """
    Exchange rate between two currencies for a given timestamp.
    """
    # Database fields
    bought_currency = ForeignKey(
        'Currency',
        related_name='rates_bought'
    )
    sold_currency = ForeignKey(
        'Currency',
        related_name='rates_sold'
    )
    value = DecimalField(
        decimal_places=2,
        max_digits=10,
        help_text="Bought units for one sold unit."
    )

    def __str__(self):
        return '{}-{}'.format(self.bought_currency, self.sold_currency)
