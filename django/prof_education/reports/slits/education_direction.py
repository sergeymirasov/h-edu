from prof_education.enrollee.models import Enrollee
from prof_education.specs.models import EducationDirection
from prof_education.students.models import Student
from prof_education.graduates.models import Graduate

from ..column_sets import ColumnSet, ColumnSetItem
from ..columns import Column
from ..filters import Choice, ChoicesFilter
from .base import Slit


class EducationDirectionSlit(Slit):
    name = "education_direction"
    label = "Направления обучения"

    def get_queryset(self):
        return EducationDirection.objects.all().with_name()

    def get_filters(self):
        return [
            ChoicesFilter(
                "education_direction_form",
                "education_form",
                "Учебная программа",
                [
                    Choice(value, label)
                    for value, label in EducationDirection.EducationForms.choices
                ],
            )
        ]

    def get_slit_key(self, data_source):
        if data_source.model is Enrollee:
            return "directions__specialization"
        elif data_source.model is Student:
            return "specialization"
        elif data_source.model is Graduate:
            return "specialization"
        raise ValueError

    def get_columns(self):
        return [
            Column("name", "Профессия"),
        ]

    def get_columnsets(self):
        return [
            ColumnSet(
                "education_direction_info",
                "Информация об образовательной программе",
                [ColumnSetItem("name")],
            )
        ]
