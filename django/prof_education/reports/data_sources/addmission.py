from django.db.models import Avg, Count

from prof_education.enrollee.models import Enrollee

from ..column_sets import ColumnFormats, ColumnSet, ColumnSetItem
from ..columns import AggrColumn, FloatAggrColumn, IntegerAggrColumn
from ..filters import NumberFilter
from .base import ColumnGroup, DataSource
from .utils import count_true


class AdmissionDataSource(DataSource):
    name = "admission"
    label = "Приемная кампания"
    model = Enrollee

    def get_filters(self):
        return [
            NumberFilter("enrollee_age", "age", "Возраст поступающих"),
        ]

    def get_columns_query_groups(self):
        enrollee_query = Enrollee.objects.with_age()
        students_query = enrollee_query.filter(status=Enrollee.Statuses.student)
        return [
            ColumnGroup(
                "enrollee_query",
                enrollee_query,
                [
                    "enrollee_count",
                    "enrollee_age_avg",
                    "enrollee_credentials_avg",
                    "enrollee_orphans",
                    "enrollee_handicapped",
                ],
            ),
            ColumnGroup(
                "students_query",
                students_query,
                [
                    "students_count",
                    "students_age_avg",
                    "students_credentials_avg",
                    "students_orphans",
                    "students_handicapped",
                ],
            ),
        ]

    def get_columns(self):
        return [
            AggrColumn("enrollee_count", "Принято документов", Count("*"), self),
            IntegerAggrColumn("enrollee_age_avg", "Средний возраст", Avg("age"), self),
            FloatAggrColumn(
                "enrollee_credentials_avg",
                "Средний балл аттестата",
                Avg("education_doc__grade"),
                self,
            ),
            AggrColumn(
                "enrollee_orphans", "Прием детей-сирот", count_true("is_orphan"), self
            ),
            AggrColumn(
                "enrollee_handicapped",
                "Прием детей-инвалидов",
                count_true("is_handicapped"),
                self,
            ),
            AggrColumn("students_count", "Факт приема", Count("*"), self),
            IntegerAggrColumn("students_age_avg", "Средний возраст", Avg("age"), self),
            FloatAggrColumn(
                "students_credentials_avg",
                "Средний балл аттестата",
                Avg("education_doc__grade"),
                self,
            ),
            AggrColumn(
                "students_orphans", "Прием детей-сирот", count_true("is_orphan"), self
            ),
            AggrColumn(
                "students_handicapped",
                "Прием детей-инвалидов",
                count_true("is_handicapped"),
                self,
            ),
        ]

    def get_columnsets(self):
        return [
            ColumnSet(
                "admission",
                "Прием документов",
                [
                    ColumnSetItem("enrollee_count", [ColumnFormats.emphasis]),
                    ColumnSetItem("enrollee_credentials_avg", [ColumnFormats.emphasis]),
                    ColumnSetItem("enrollee_orphans"),
                    ColumnSetItem("enrollee_handicapped"),
                    ColumnSetItem("enrollee_age_avg"),
                ],
            ),
            ColumnSet(
                "enrollment",
                "Зачисление",
                [
                    ColumnSetItem("students_count", [ColumnFormats.emphasis]),
                    ColumnSetItem("students_credentials_avg", [ColumnFormats.emphasis]),
                    ColumnSetItem("students_orphans"),
                    ColumnSetItem("students_handicapped"),
                    ColumnSetItem("students_age_avg"),
                ],
            ),
        ]
