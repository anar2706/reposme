from django.db import models
from django.utils.translation import gettext_lazy as _


class County(models.Model):

    country_choices = {
        1: _('Azerbaijan')
    }

    county = models.CharField(max_length=120, db_index=True)
    country = models.IntegerField(choices=tuple(country_choices.items()), default=1)

    def __str__(self):
        return f"{self.county}, {self.country_choices[self.country]}"

    class Meta:
        ordering = ['country', 'county']