from django.db import models
from django.utils.translation import gettext as _


class ia(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, default=None)
    location = models.CharField(max_length=100, blank=True, null=True, default=None)
    post = models.CharField(max_length=100, default=None)
    company = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=100, blank=True, null=True, default=None)
    url = models.URLField(max_length=200)

