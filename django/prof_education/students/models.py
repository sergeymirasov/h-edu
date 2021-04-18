from django.db import models
from django.db.models import Case, ExpressionWrapper, F, Value, When
from django.utils import timezone
from django.utils.translation import gettext as _


class StudentStatuses(models.TextChoices):
    learns = "learns", "Обучается"
    is_excluded = "is_excluded", "Отчислен"
    is_due = "is_due", "Окончил"


class StudentQuerySet(models.QuerySet):
    def with_status(self):
        return self.annotate(
            status=Case(
                When(due_at__isnull=False, then=Value(StudentStatuses.is_due)),
                When(
                    excluded_at__isnull=False, then=Value(StudentStatuses.is_excluded)
                ),
                default=Value(StudentStatuses.learns),
            )
        )

    def with_age(self):
        return self.annotate(
            age=ExpressionWrapper(
                Value(timezone.now().date().year) - F("birth_date__year"),
                output_field=models.IntegerField(),
            )
        )


class Student(models.Model):
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
    admitted_at = models.DateField(
        _("Дата поступления"), auto_now=False, auto_now_add=False
    )
    due_at = models.DateField(
        _("Дата окончания"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    excluded_at = models.DateField(
        _("Дата исключения"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    in_residence = models.BooleanField(_("Проживают в общежитии"))
    is_orphan = models.BooleanField(
        _("Дети-сироты, дети, оставшиеся без попечения родителей, лица из их числа")
    )
    is_handicapped = models.BooleanField(_("Инвалиды"))
    is_ovz = models.BooleanField(_("Лица с ОВЗ (имеется ПМПК)"))

    class Sexes(models.IntegerChoices):
        male = 0, "Мужской"
        female = 1, "Женский"

    sex = models.PositiveSmallIntegerField("Пол", choices=Sexes.choices, db_index=True)

    objects = StudentQuerySet.as_manager()

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
