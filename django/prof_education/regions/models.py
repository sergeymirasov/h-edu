from django.db import models
from django.utils.translation import gettext as _


class Region(models.Model):
    name = models.CharField(_("Регион"), max_length=128)

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self):
        return self.name
