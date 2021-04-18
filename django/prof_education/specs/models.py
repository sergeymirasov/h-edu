from django.db import models
from django.db.models import Case, ExpressionWrapper, F, Value, When
from django.db.models.functions import Concat
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


class EducationDirectionQuerySet(models.QuerySet):
    def with_name(self):
        return self.annotate(
            name=Concat(
                F("specialization__name"),
                Value(" "),
                Case(
                    When(education_form="full_time", then=Value("(оч.)")),
                    When(education_form="part_time", then=Value("(заоч.)")),
                    When(education_form="distance", then=Value("(о.з.)")),
                ),
            )
        )


class EducationDirection(models.Model):
    specialization = models.ForeignKey(
        "Specialization",
        verbose_name=_("Специальность"),
        on_delete=models.CASCADE,
        related_name="directions",
        db_index=True,
    )

    class EducationForms(models.TextChoices):
        full_time = "full_time", "Очная"
        part_time = "part_time", "Очно-заочная"
        distance = "distance", "Заочная"

    education_form = models.CharField(
        _("Форма обучения"),
        max_length=count_max_length(EducationForms),
        choices=EducationForms.choices,
        db_index=True,
    )
    duration = models.PositiveSmallIntegerField(
        _("Продолжительность"), help_text="В месяцах"
    )

    objects = EducationDirectionQuerySet.as_manager()

    class Meta:
        verbose_name = "Направление обучения"
        verbose_name_plural = "Направления обучения"
        unique_together = ("specialization", "education_form")
