from django.db import models
from django.utils.translation import ugettext_lazy as _

from prof_education.utils.choices import count_max_length


class Specialization(models.Model):
    codifier = models.CharField(_("Кодификатор"), max_length=50, unique=True)
    name = models.CharField(_("Название"), max_length=128)

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return f"{self.codifier} {self.name}"


class EducationDirection(models.Model):
    specialization = models.ForeignKey(
        "Specialization",
        verbose_name=_("Специальность"),
        on_delete=models.CASCADE,
        related_name="directions",
    )

    class EducationForms(models.TextChoices):
        full_time = "full_time", "Очная"
        part_time = "part_time", "Очно-заочная"
        distance = "distance", "Заочная"

    education_form = models.CharField(
        _("Форма обучения"),
        max_length=count_max_length(EducationForms),
        choices=EducationForms.choices,
    )
    duration = models.PositiveSmallIntegerField(
        _("Продолжительность"), help_text="В месяцах"
    )

    class Meta:
        verbose_name = "Направление обучения"
        verbose_name_plural = "Направления обучения"
        unique_together = ("specialization", "education_form")
