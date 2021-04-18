from django.db.models import Avg, Count

from prof_education.regions.models import Region
from prof_education.students.models import Student

from ..column_sets import ColumnFormats, ColumnSet, ColumnSetItem
from ..columns import AggrColumn, IntegerAggrColumn
from ..filters import ModelChoicesFilter, NumberFilter
from .base import ColumnGroup, DataSource
from .utils import count_true, count_value


class StudentsDataSource(DataSource):
    name = "students"
    label = "Студенты"
    model = Student

    def get_filters(self):
        return [
            NumberFilter("student_age", "age", "Возраст студентов"),
        ]

    def get_columns(self):
        return [
            AggrColumn("student_count", "Всего", Count("*"), self),
            IntegerAggrColumn("student_age_avg", "Средний возраст", Avg("age"), self),
            IntegerAggrColumn(
                "student_in_residence",
                "Проживают в обжещитии",
                count_true("in_residence"),
                self,
            ),
            IntegerAggrColumn(
                "student_is_orphan", "Сироты", count_true("is_orphan"), self
            ),
            IntegerAggrColumn(
                "student_is_handicapped", "Инвалиды", count_true("is_handicapped"), self
            ),
            IntegerAggrColumn(
                "student_male",
                "Мужчины",
                count_value("sex", Student.Sexes.male),
                self,
            ),
            IntegerAggrColumn(
                "student_female",
                "Женщины",
                count_value("sex", Student.Sexes.female),
                self,
            ),
            AggrColumn("excluded_count", "Всего", Count("*"), self),
            IntegerAggrColumn("excluded_age_avg", "Средний возраст", Avg("age"), self),
            IntegerAggrColumn(
                "excluded_in_residence",
                "Проживали в обжещитии",
                count_true("in_residence"),
                self,
            ),
            IntegerAggrColumn(
                "excluded_is_orphan", "Сироты", count_true("is_orphan"), self
            ),
            IntegerAggrColumn(
                "excluded_is_handicapped",
                "Инвалиды",
                count_true("is_handicapped"),
                self,
            ),
            IntegerAggrColumn(
                "excluded_male",
                "Мужчины",
                count_value("sex", Student.Sexes.male),
                self,
            ),
            IntegerAggrColumn(
                "excluded_female",
                "Женщины",
                count_value("sex", Student.Sexes.female),
                self,
            ),
        ]

    def get_columnsets(self):
        return [
            ColumnSet(
                "students",
                "Обучающиеся",
                [
                    ColumnSetItem("student_count", [ColumnFormats.emphasis]),
                    ColumnSetItem("student_age_avg"),
                    ColumnSetItem("student_in_residence"),
                    ColumnSetItem("student_is_orphan"),
                    ColumnSetItem("student_is_handicapped"),
                    ColumnSetItem("student_male"),
                    ColumnSetItem("student_female"),
                ],
            ),
            ColumnSet(
                "excluded",
                "Выбыло",
                [
                    ColumnSetItem("excluded_count", [ColumnFormats.emphasis]),
                    ColumnSetItem("excluded_age_avg"),
                    ColumnSetItem("excluded_in_residence"),
                    ColumnSetItem("excluded_is_orphan"),
                    ColumnSetItem("excluded_is_handicapped"),
                    ColumnSetItem("excluded_male"),
                    ColumnSetItem("excluded_female"),
                ],
            ),
        ]

    def get_columns_query_groups(self):
        students_query = Student.objects.with_age().with_status()
        learns_query = students_query.filter(status="learns")
        excluded_query = students_query.filter(status="is_excluded")
        return [
            ColumnGroup(
                "learns_query",
                learns_query,
                [
                    "student_count",
                    "student_age_avg",
                    "student_in_residence",
                    "student_is_orphan",
                    "student_is_handicapped",
                    "student_male",
                    "student_female",
                ],
            ),
            ColumnGroup(
                "excluded_query",
                excluded_query,
                [
                    "excluded_count",
                    "excluded_age_avg",
                    "excluded_in_residence",
                    "excluded_is_orphan",
                    "excluded_is_handicapped",
                    "excluded_male",
                    "excluded_female",
                ],
            ),
        ]
