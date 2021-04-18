import random
from datetime import date

import factory
from faker import Factory as FakerFactory

from prof_education.organizations.models import EducationOrg
from prof_education.specs.models import EducationDirection
from prof_education.utils.factory import choice_with_chance

from .models import Student

faker = FakerFactory.create(locale="ru_RU")


class StudentFactory(factory.django.DjangoModelFactory):
    sex = factory.LazyAttribute(lambda x: random.choice([0, 1]))
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
    specialization = factory.LazyAttribute(
        lambda x: random.choice(EducationDirection.objects.all())
    )
    education_org = factory.LazyAttribute(
        lambda x: random.choice(EducationOrg.objects.all())
    )
    admitted_at = factory.LazyAttribute(
        lambda x: faker.date_between_dates(
            date_start=date(2016, 1, 1), date_end=date(2021, 1, 1)
        )
    )
    due_at = factory.LazyAttribute(
        lambda x: choice_with_chance(
            5,
            faker.date_between_dates(
                date_start=x.admitted_at, date_end=date(2021, 1, 1)
            ),
        )
    )
    excluded_at = factory.LazyAttribute(
        lambda x: None
        if x.due_at
        else choice_with_chance(
            5,
            faker.date_between_dates(
                date_start=x.admitted_at, date_end=date(2021, 1, 1)
            ),
        )
    )
    in_residence = factory.LazyAttribute(lambda x: choice_with_chance(5, True, False))
    is_orphan = factory.LazyAttribute(lambda x: choice_with_chance(15, True, False))
    is_handicapped = factory.LazyAttribute(
        lambda x: choice_with_chance(30, True, False)
    )
    is_ovz = factory.LazyAttribute(lambda x: choice_with_chance(50, True, False))

    class Meta:
        model = Student
