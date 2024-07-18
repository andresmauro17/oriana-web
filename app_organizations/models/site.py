# django imports
from django.db import models

# Utilities
from config.utils.models import CustomBaseModel

# Django models
from app_organizations.models import Organization


class SiteQuerySet(models.query.QuerySet):
    def get_active(self):
        return self.filter(is_active=True)


class SiteManager(models.Manager):
    def get_queryset(self):
        return SiteQuerySet(self.model, using=self._db)

    def get_active(self):
        return self.get_queryset().get_active()


class Site(CustomBaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,)
    organization = models.ForeignKey(Organization, related_name='sites', on_delete = models.CASCADE)
    empresa_id_amarey = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    objects = SiteManager()

    @property
    def get_site_org(self):
        return f'{self.organization.name} {self.organization.city}| {self.name}'

    def __str__(self):
        # return self.name + "|" + self.organization.name
        return f'{self.organization.name} {self.organization.city}| {self.name}'
