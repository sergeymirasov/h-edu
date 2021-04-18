from django.db.models import Avg, Count

from prof_education.graduates.models import Graduate

from ..column_sets import ColumnFormats, ColumnSet, ColumnSetItem
from ..columns import AggrColumn, IntegerAggrColumn
from ..filters import NumberFilter
from .base import ColumnGroup, DataSource
from .utils import count_value


class GraduatesDataSource(DataSource):
    name = "graduates"
    label = "Выпускники"
    model = Graduate

    def get_filters(self):
        return [
            NumberFilter("graduates_age", "age", "Возраст выпускников"),
        ]

    def get_columns(self):
        return [
            AggrColumn("graduates_count", "Всего", Count("*"), self),
            IntegerAggrColumn("graduates_age_avg", "Средний возраст", Avg("age"), self),
            IntegerAggrColumn(
                "graduates_male",
                "Мужчины",
                count_value("sex", Graduate.Sexes.male),
                self,
            ),
            IntegerAggrColumn(
                "graduates_female",
                "Женщины",
                count_value("sex", Graduate.Sexes.female),
                self,
            ),
            AggrColumn(
                "employed_count",
                "Трудоустроены",
                count_value("status", "employed"),
                self,
            ),
            AggrColumn(
                "employed_by_contract_count",
                "Трудоустроены согласно целевым договорам",
                count_value("status", "employed_by_contract"),
                self,
            ),
            AggrColumn(
                "continue_education_count",
                "Продолжили обучение",
                count_value("status", "continue_education"),
                self,
            ),
            AggrColumn(
                "not_employed_count",
                "Не трудоустроены",
                count_value("status", "not_employed"),
                self,
            ),
        ]

    def get_columnsets(self):
        return [
            ColumnSet(
                "graduates",
                "Выпускники",
                [
                    ColumnSetItem("graduates_count", [ColumnFormats.emphasis]),
                    ColumnSetItem("graduates_age_avg"),
                    ColumnSetItem("graduates_male"),
                    ColumnSetItem("graduates_female"),
                ],
            ),
            ColumnSet(
                "status",
                "Из них",
                [
                    ColumnSetItem("employed_count", [ColumnFormats.emphasis]),
                    ColumnSetItem(
                        "employed_by_contract_count", [ColumnFormats.emphasis]
                    ),
                    ColumnSetItem("continue_education_count"),
                    ColumnSetItem("not_employed_count"),
                ],
            ),
        ]

    def get_columns_query_groups(self):
        graduates_query = Graduate.objects.with_age()
        return [
            ColumnGroup(
                "graduates_query",
                graduates_query,
                [
                    "graduates_count",
                    "graduates_age_avg",
                    "graduates_male",
                    "graduates_female",
                    "employed_count",
                    "employed_by_contract_count",
                    "continue_education_count",
                    "not_employed_count",
                ],
            ),
        ]
