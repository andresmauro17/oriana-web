# django imports
from django.db import models

# Utilities
from config.utils.models import CustomBaseModel

# Django models
from app_organizations.models import Organization

class Site(CustomBaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,)
    organization = models.ForeignKey(Organization, related_name='sites', on_delete = models.CASCADE)
    empresa_id_amarey = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        # return self.name + "|" + self.organization.name
        return f'{self.organization.name} {self.organization.city}| {self.name}'
