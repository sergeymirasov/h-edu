from django.db import models
from django.utils.translation import gettext_lazy as _


class EducationOrg(models.Model):
    name = models.CharField(_("Наименование"), max_length=128)
    region = models.ForeignKey(
        "regions.Region",
        verbose_name=_("Регион"),
        on_delete=models.CASCADE,
        null=True,
        db_index=True,
    )

    class Meta:
        verbose_name = "Образовательное учреждение"
        verbose_name_plural = "Образовательные учреждения"

    def __str__(self):
        return self.name
