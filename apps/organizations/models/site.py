# django imports
from django.db import models

# Utilities
from config.utils.models import CustomBaseModel

# Django models
from apps.organizations.models import Organization

class Site(CustomBaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,)
    organization = models.ForeignKey(Organization, on_delete = models.CASCADE)
