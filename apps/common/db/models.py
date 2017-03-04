"""
Common models functionality and base classes.
"""
from django.db.models import ForeignKey, Model


class OwnedEntity(Model):
    """
    Base model for all objects that are owned by a group.
    """
    class Meta(object):
        abstract = True

    # Database fields
    domain = ForeignKey('auth.Group')
