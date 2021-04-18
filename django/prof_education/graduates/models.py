from django.db import models
from django.db.models import ExpressionWrapper, F, Value
from django.utils import timezone
from django.utils.translation import gettext as _

from prof_education.utils.choices import count_max_length


class GraduateQuerySet(models.QuerySet):
    def with_age(self):
        return self.annotate(
            age=ExpressionWrapper(
                Value(timezone.now().date().year) - F("birth_date__year"),
                output_field=models.IntegerField(),
            )
        )


class Graduate(models.Model):
    first_name = models.CharField(_("Имя"), max_length=128)
    last_name = models.CharField(_("Фамилия"), max_length=128)
    middle_name = models.CharField(_("Отчество"), max_length=128)
    birth_date = models.DateField(
        _("Дата рождения"), auto_now=False, auto_now_add=False
    )
    specialization = models.ForeignKey(
        "specs.EducationDirection",
        verbose_name=_("Специализация"),
        on_delete=models.CASCADE,
    )
    education_org = models.ForeignKey(
        "organizations.EducationOrg",
        verbose_name=_("Образовательное учреждение"),
        on_delete=models.CASCADE,
    )
    due_at = models.DateField(
        _("Дата окончания"), auto_now=False, auto_now_add=False, blank=True, null=True
    )

    class EducationForms(models.TextChoices):
        budget = "budget", "Бюджетная"
        contract = "contract", "Платная основа"

    education_form = models.CharField(
        _("Форма обучения"),
        choices=EducationForms.choices,
        max_length=count_max_length(EducationForms),
    )

    class Sexes(models.IntegerChoices):
        male = 0, "Мужской"
        female = 1, "Женский"

    sex = models.PositiveSmallIntegerField("Пол", choices=Sexes.choices, db_index=True)

    class Statuses(models.TextChoices):
        employed = "employed", "Трудоустроены"
        employed_by_contract = (
            "employed_by_contract",
            "Трудустроены согласно целевым договорам",
        )
        continue_education = "continue_education", "Продолжили обучение"
        not_employed = "not_employed", "Не трудоустроены"

    status = models.CharField(
        "Статус", max_length=count_max_length(Statuses), choices=Statuses.choices
    )

    objects = GraduateQuerySet.as_manager()

    class Meta:
        verbose_name = "Выпускник"
        verbose_name_plural = "Выпускники"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
