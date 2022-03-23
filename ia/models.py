from django.db import models
from adaptor.model import CsvModel
from adaptor.fields import CharField
from django.utils.translation import gettext as _


class Ia(CsvModel):
    name = CharField(max_length=100)
    description = CharField(blank=True, null=True, default=None)
    location = CharField(max_length=100, blank=True, null=True, default=None)
    post = CharField(max_length=100, default=None)
    company = CharField(max_length=100, default=None)
    email = CharField(max_length=100, blank=True, null=True, default=None)
    url_profile = CharField(max_length=200)

    class Meta:
        delimiter = ","
