from django.db import models
from django.db.models import ExpressionWrapper, F, Value
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from prof_education.utils.choices import count_max_length


class EnrolleeQuerySet(models.QuerySet):
    def with_age(self):
        return self.annotate(
            age=ExpressionWrapper(
                Value(timezone.now().date().year) - F("birth_date__year"),
                output_field=models.IntegerField(),
            )
        )


class Enrollee(models.Model):
    first_name = models.CharField(_("Имя"), max_length=128)
    last_name = models.CharField(_("Фамилия"), max_length=128)
    middle_name = models.CharField(_("Отчество"), max_length=128)
    birth_date = models.DateField(
        _("Дата рождения"), auto_now=False, auto_now_add=False, db_index=True
    )
    birth_place = models.CharField(_("Место рождения"), max_length=128)
    # fixme: более точные гражданства, возможно из списка
    citizenship = models.CharField(_("Гражданство"), max_length=128)
    passport = models.OneToOneField(
        "EnrolleePassport", verbose_name=_("Паспорт"), on_delete=models.CASCADE
    )
    residence_place = models.CharField(_("Место проживания"), max_length=256)
    personal_phone = models.CharField(_("Личный телефон"), max_length=50)
    home_phone = models.CharField(
        _("Домашний телефон"), max_length=50, blank=True, null=True
    )
    graduated_institution = models.OneToOneField(
        "GraduatedInstitution",
        on_delete=models.CASCADE,
        verbose_name="Окончил",
        blank=True,
        null=True,
    )
    education_org = models.ForeignKey(
        "organizations.EducationOrg",
        verbose_name=_("Образовательная организация"),
        on_delete=models.CASCADE,
        db_index=True,
    )

    class Grades(models.IntegerChoices):
        five_classes = 0, "5 классов"
        nine_classes = 1, "9 классов"
        eleven_classes = 2, "11 классов"
        special = 3, "Среднее специальное образование"
        incomplete_higher = 4, "Неоконченное высшее"
        higher = 5, "Высшее"

    grade = models.PositiveSmallIntegerField(
        _("Уровень образование"), choices=Grades.choices, db_index=True
    )
    education_doc = models.OneToOneField(
        "EducationDoc",
        verbose_name=_("Документ об образовании"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
    )
    english = models.BooleanField(_("Английский язык"), db_index=True)
    has_goal_contract = models.BooleanField(
        _("Наличие договора о целевом обучении"), db_index=True
    )
    gos_olympiad_status = models.OneToOneField(
        "GosOlympiadStatus",
        verbose_name=_("Участие в государственных олимпиадах"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
    )
    wsr_olympiad_status = models.OneToOneField(
        "WsrOlympiadStatus",
        verbose_name=_('Участие в чемпионате "Молодые профессионалы (WSR)"'),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
    )
    abylimpix_status = models.OneToOneField(
        "AbylimpixStatus",
        verbose_name=_('Участие в чемпионате "Абилимпикс"'),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
    )
    need_residence = models.BooleanField(_("Общежитие"), db_index=True)
    is_orphan = models.BooleanField(
        _("Дети-сироты, дети, оставшиеся без попечения родителей, лица из их числа"),
        db_index=True,
    )
    is_handicapped = models.BooleanField(_("Инвалиды"), db_index=True)
    is_ovz = models.BooleanField(_("Лица с ОВЗ (имеется ПМПК)"), db_index=True)

    choreography_doc = models.CharField(
        _("Хореография (подтверждающий документ)"),
        max_length=128,
        blank=True,
        null=True,
    )
    vocal_doc = models.CharField(
        _("Вокальные данные (подтверждающий документ)"),
        max_length=128,
        blank=True,
        null=True,
    )
    kvn_doc = models.CharField(
        _("Участие в КВН (подтверждающий документ)"),
        max_length=128,
        blank=True,
        null=True,
    )
    art_doc = models.CharField(
        _("Художественные навыки (подтверждающий документ)"),
        max_length=128,
        blank=True,
        null=True,
    )
    theatre_doc = models.CharField(
        _("Участие в театральных постановках (подтверждающий документ)"),
        max_length=128,
        blank=True,
        null=True,
    )

    mother = models.OneToOneField(
        "ParentData",
        verbose_name=_("Сведения о матери"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
    )
    father = models.OneToOneField(
        "ParentData",
        verbose_name=_("Сведения об отце"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
    )
    parents_email = models.EmailField(
        _("Адрес электронной почты родителей"), max_length=254
    )
    is_first_time = models.BooleanField(
        _("Среднее профессиональное образование получаю впервые")
    )
    application_dt = models.DateTimeField(
        _("Дата подачи заявления"), default=timezone.now, editable=False
    )

    class Sexes(models.IntegerChoices):
        male = 0, "Мужской"
        female = 1, "Женский"

    sex = models.PositiveSmallIntegerField("Пол", choices=Sexes.choices, db_index=True)

    class Statuses(models.TextChoices):
        enrollee = "enrollee", "Абитуриент"
        student = "student", "Студент"
        rejected = "rejected", "Не поступил"

    status = models.CharField(
        "Статус",
        default=Statuses.enrollee,
        choices=Statuses.choices,
        max_length=count_max_length(Statuses),
    )

    objects = EnrolleeQuerySet.as_manager()

    class Meta:
        verbose_name = "Абитуриент"
        verbose_name_plural = "Абитуриенты"
        ordering = ("-application_dt",)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class EnrolleePassport(models.Model):
    series = models.CharField(_("Серия"), max_length=4)
    num = models.CharField(_("№"), max_length=6)
    issued_at = models.DateField(_("Когда выдан"), auto_now=False, auto_now_add=False)
    issued_by = models.CharField(_("Кем выдан"), max_length=128)

    class Meta:
        verbose_name = "Паспорт поступающего"
        verbose_name_plural = "Паспорта поступающих"


class EnrolleeSpecialization(models.Model):
    priority = models.SmallIntegerField(_("Приоритет"), db_index=True)
    specialization = models.ForeignKey(
        "specs.EducationDirection",
        verbose_name=_("Специализация"),
        on_delete=models.CASCADE,
        db_index=True,
    )

    class EducationForms(models.TextChoices):
        budget = "budget", "Бюджетная"
        contract = "contract", "Платная основа"

    education_form = models.CharField(
        _("Форма обучения"),
        choices=EducationForms.choices,
        max_length=count_max_length(EducationForms),
    )
    enrollee = models.ForeignKey(
        "Enrollee",
        verbose_name=_("Абитуриент"),
        on_delete=models.CASCADE,
        related_name="directions",
    )

    class Meta:
        verbose_name = "Специализация абитуриента"
        verbose_name_plural = "Специализации абитуриентов"
        ordering = ("priority",)
        unique_together = ("priority", "enrollee")


class GraduatedInstitution(models.Model):
    graduated_at = models.CharField(_("Год окончания"), max_length=4)
    institution = models.CharField(_("Учреждение"), max_length=256)

    class Meta:
        verbose_name = "Оконченное учебное заведение"
        verbose_name_plural = "Оконченные учебные заведения"


class OlympiadStatuses(models.TextChoices):
    medalist = "medalist", "Призер"
    winner = "winner", "Победитель"


class GosOlympiadStatus(models.Model):
    status = models.CharField(
        _("Статус"),
        max_length=count_max_length(OlympiadStatuses),
        choices=OlympiadStatuses.choices,
    )

    class Levels(models.TextChoices):
        country = "country", "Всероссийской"
        region = "region", "Областной"

    level = models.CharField(
        _("Уровень"), max_length=count_max_length(Levels), choices=Levels.choices
    )
    subject = models.CharField(_("Наименование предмета"), max_length=50)

    class Meta:
        verbose_name = "Участие в государственных олимпиадах"
        verbose_name_plural = "Участие в государственных олимпиадах"


class WsrOlympiadStatus(models.Model):
    status = models.CharField(
        _("Статус"),
        max_length=count_max_length(OlympiadStatuses),
        choices=OlympiadStatuses.choices,
    )
    competition = models.CharField(_("Компетенция"), max_length=128)

    class Meta:
        verbose_name = 'Участие в чемпионате "Молодые профессионалы (WSR)"'
        verbose_name_plural = 'Участие в чемпионате "Молодые профессионалы (WSR)"'


class AbylimpixStatus(models.Model):
    status = models.CharField(
        _("Статус"),
        max_length=count_max_length(OlympiadStatuses),
        choices=OlympiadStatuses.choices,
    )
    competition = models.CharField(_("Компетенция"), max_length=128)

    class Meta:
        verbose_name = 'Участие в чемпионате "Абилимпикс"'
        verbose_name_plural = 'Участие в чемпионате "Абилимпикс"'


class SportAchievement(models.Model):
    type = models.CharField(_("Вид спорта"), max_length=128)
    approve_doc = models.CharField(_("Подтверждающий документ"), max_length=128)
    enrollee = models.ForeignKey(
        "Enrollee",
        verbose_name=_("Абитуриент"),
        on_delete=models.CASCADE,
        related_name="sport_achievements",
    )

    class Meta:
        verbose_name = "Спортивное достижение"
        verbose_name_plural = "Спортивные достижения"


class ParentData(models.Model):
    first_name = models.CharField(_("Имя"), max_length=128)
    last_name = models.CharField(_("Фамилия"), max_length=128)
    middle_name = models.CharField(_("Отчество"), max_length=128)
    # fixme: можно сделать автозаполнение
    residence = models.CharField(_("Место жительства"), max_length=128)
    enterprise_name = models.CharField(
        _("Наименование предприятия"), max_length=128, blank=True, null=True
    )
    position_held = models.CharField(
        _("Занимаемая позиция"), max_length=128, blank=True, null=True
    )
    phone = models.CharField(_("Личный контактный телефон"), max_length=50)

    class Meta:
        verbose_name = "Информация о родителях"
        verbose_name_plural = "Информация о родителях"


class EducationDoc(models.Model):
    class Types(models.TextChoices):
        credential = "credential", "Аттестат"

    type = models.CharField(
        _("Тип"), max_length=count_max_length(Types), choices=Types.choices
    )
    num = models.CharField(_("Номер"), max_length=50)
    grade = models.PositiveSmallIntegerField(_("Оценка"), db_index=True)

    class Meta:
        verbose_name = "Документ об образовании"
        verbose_name_plural = "Документы об образовании"
