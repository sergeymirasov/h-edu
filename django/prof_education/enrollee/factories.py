import random
from datetime import date

import factory
from faker import Factory as FakerFactory

from prof_education.organizations.models import EducationOrg
from prof_education.specs.models import EducationDirection
from prof_education.utils.factory import choice_with_chance, random_bool, random_digits

from .models import (
    AbylimpixStatus,
    EducationDoc,
    Enrollee,
    EnrolleePassport,
    EnrolleeSpecialization,
    GosOlympiadStatus,
    GraduatedInstitution,
    ParentData,
    SportAchievement,
    WsrOlympiadStatus,
)

faker = FakerFactory.create(locale="ru_RU")


subjects = ["Математика", "Обществознание", "Биология", "Русский язык", "Литература"]

sport_types = ["Футбол", "Баскетбол", "Волейбол", "Бег"]


class PassportFactory(factory.django.DjangoModelFactory):
    series = factory.LazyAttribute(lambda x: random_digits(4))
    num = factory.LazyAttribute(lambda x: random_digits(6))
    issued_at = factory.LazyAttribute(
        lambda x: faker.date_between_dates(
            date_start=date(1998, 1, 1), date_end=date(2005, 1, 1)
        )
    )
    issued_by = factory.LazyAttribute(lambda x: faker.city())

    class Meta:
        model = EnrolleePassport


class GraduatedInstitutionFactory(factory.django.DjangoModelFactory):
    graduated_at = factory.LazyAttribute(lambda x: str(random.randint(2015, 2020)))
    institution = factory.LazyAttribute(
        lambda x: f"Школа №{random.randint(1, 10)} г. Томска"
    )

    class Meta:
        model = GraduatedInstitution


class EducationDocFactory(factory.django.DjangoModelFactory):
    type = "credential"
    num = factory.LazyAttribute(lambda x: random_digits(8))
    grade = factory.LazyAttribute(lambda x: random.randint(0, 10))

    class Meta:
        model = EducationDoc


class GosOlympiadStatusFactory(factory.django.DjangoModelFactory):
    status = factory.LazyAttribute(lambda x: random.choice(["medalist", "winner"]))
    level = factory.LazyAttribute(lambda x: random.choice(["country", "region"]))
    subject = factory.LazyAttribute(lambda x: random.choice(subjects))

    class Meta:
        model = GosOlympiadStatus


class WsrOlympiadStatusFactory(factory.django.DjangoModelFactory):
    status = factory.LazyAttribute(lambda x: random.choice(["medalist", "winner"]))
    competition = factory.LazyAttribute(lambda x: random.choice(subjects))

    class Meta:
        model = WsrOlympiadStatus


class AbylimpixStatusFactory(factory.django.DjangoModelFactory):
    status = factory.LazyAttribute(lambda x: random.choice(["medalist", "winner"]))
    competition = factory.LazyAttribute(lambda x: random.choice(subjects))

    class Meta:
        model = AbylimpixStatus


class EnrolleeFactory(factory.django.DjangoModelFactory):
    sex = factory.Sequence(lambda x: random.choice([0, 1]))
    first_name = factory.LazyAttribute(
        lambda x: faker.first_name_male() if x.sex == 0 else faker.first_name_female()
    )
    last_name = factory.LazyAttribute(
        lambda x: faker.last_name_male() if x.sex == 0 else faker.last_name_female()
    )
    middle_name = factory.LazyAttribute(
        lambda x: faker.middle_name_male() if x.sex == 0 else faker.middle_name_female()
    )
    birth_date = factory.LazyAttribute(
        lambda x: faker.date_between_dates(
            date_start=date(1998, 1, 1), date_end=date(2005, 1, 1)
        )
    )
    birth_place = factory.LazyAttribute(lambda x: faker.city())
    citizenship = "Российская Федерация"
    passport = factory.SubFactory(PassportFactory)
    residence_place = factory.LazyAttribute(lambda x: faker.address())
    personal_phone = factory.LazyAttribute(lambda x: faker.phone_number())
    home_phone = factory.LazyAttribute(
        lambda x: random.choice([None, faker.phone_number()])
    )
    graduated_institution = factory.SubFactory(GraduatedInstitutionFactory)
    education_org = factory.LazyAttribute(
        lambda x: random.choice(EducationOrg.objects.all())
    )
    grade = factory.LazyAttribute(lambda x: random.randint(0, 5))
    education_doc = factory.LazyAttribute(
        lambda x: random.choice([None, EducationDocFactory()])
    )
    english = factory.LazyAttribute(lambda x: random_bool())
    has_goal_contract = factory.LazyAttribute(lambda x: random_bool())
    gos_olympiad_status = factory.LazyAttribute(
        lambda x: choice_with_chance(10, GosOlympiadStatusFactory)
    )
    wsr_olympiad_status = factory.LazyAttribute(
        lambda x: choice_with_chance(10, WsrOlympiadStatusFactory)
    )
    abylimpix_status = factory.LazyAttribute(
        lambda x: choice_with_chance(10, AbylimpixStatusFactory)
    )
    need_residence = factory.LazyAttribute(lambda x: choice_with_chance(3, True, False))
    is_orphan = factory.LazyAttribute(lambda x: choice_with_chance(15, True, False))
    is_handicapped = factory.LazyAttribute(
        lambda x: choice_with_chance(20, True, False)
    )
    is_ovz = factory.LazyAttribute(lambda x: choice_with_chance(40, True, False))
    choreography_doc = factory.LazyAttribute(
        lambda x: choice_with_chance(5, random_digits(6))
    )
    vocal_doc = factory.LazyAttribute(lambda x: choice_with_chance(5, random_digits(6)))
    kvn_doc = factory.LazyAttribute(lambda x: choice_with_chance(5, random_digits(6)))
    art_doc = factory.LazyAttribute(lambda x: choice_with_chance(5, random_digits(6)))
    theatre_doc = factory.LazyAttribute(
        lambda x: choice_with_chance(5, random_digits(6))
    )
    mother = factory.LazyAttribute(lambda x: ParentDataFactory(sex="female"))
    father = factory.LazyAttribute(lambda x: ParentDataFactory(sex="male"))
    parents_email = factory.LazyAttribute(lambda x: faker.ascii_email())
    is_first_time = factory.LazyAttribute(lambda x: choice_with_chance(20, False, True))
    status = factory.LazyAttribute(
        lambda x: choice_with_chance(
            3, choice_with_chance(3, "student", "rejected"), "enrollee"
        )
    )

    class Meta:
        model = Enrollee

    @factory.post_generation
    def directions(obj, created, extracted, **kwargs):
        for n in range(random.randint(1, 4)):
            EnrolleeSpecializationFactory(enrollee=obj, priority=n)

    @factory.post_generation
    def sport_achievements(obj, created, extracted, **kwargs):
        for _ in range(choice_with_chance(4, random.randint(1, 3), 0)):
            SportAchievementFactory(enrollee=obj)


class ParentDataFactory(factory.django.DjangoModelFactory):
    class Params:
        sex = "male"

    first_name = factory.LazyAttribute(
        lambda x: faker.first_name_male()
        if x.sex == "male"
        else faker.first_name_female()
    )
    last_name = factory.LazyAttribute(
        lambda x: faker.last_name_male()
        if x.sex == "male"
        else faker.last_name_female()
    )
    middle_name = factory.LazyAttribute(
        lambda x: faker.middle_name_male()
        if x.sex == "male"
        else faker.middle_name_female()
    )
    residence = factory.LazyAttribute(lambda x: faker.address())
    enterprise_name = factory.LazyAttribute(lambda x: faker.company())
    position_held = factory.LazyAttribute(lambda x: faker.job())
    phone = factory.LazyAttribute(lambda x: faker.phone_number())

    class Meta:
        model = ParentData


class EnrolleeSpecializationFactory(factory.django.DjangoModelFactory):
    specialization = factory.LazyAttribute(
        lambda x: random.choice(EducationDirection.objects.all())
    )
    education_form = factory.LazyAttribute(
        lambda x: choice_with_chance(4, "contract", "budget")
    )

    class Meta:
        model = EnrolleeSpecialization


class SportAchievementFactory(factory.django.DjangoModelFactory):
    type = factory.LazyAttribute(lambda x: random.choice(sport_types))
    approve_doc = factory.LazyAttribute(lambda x: random_digits(8))

    class Meta:
        model = SportAchievement
