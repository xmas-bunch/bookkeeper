"""
Factories for models from external applications.
"""
from django.contrib.auth.models import Group
from factory import DjangoModelFactory, Faker


class GroupFactory(DjangoModelFactory):
    """
    Factory for generic group.
    """
    class Meta(object):
        model = Group

    name = Faker('word')
