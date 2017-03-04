# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Official name in home language.', max_length=100)),
                ('code', models.CharField(help_text='International, three-letter code.', max_length=3)),
                ('symbol', models.CharField(help_text='Short-hand symbol.', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, help_text='Bought units for one sold unit.', max_digits=10)),
                ('bought_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates_bought', to='currencies.Currency')),
                ('sold_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates_sold', to='currencies.Currency')),
            ],
        ),
    ]
