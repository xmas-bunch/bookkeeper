"""
Queryset and manager customizations for accounts.
"""
from django.db.models.query import QuerySet
from django_group_by import GroupByMixin


class GroupByQuerySet(QuerySet, GroupByMixin):
    pass
