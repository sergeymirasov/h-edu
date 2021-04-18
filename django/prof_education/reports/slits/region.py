from prof_education.regions.models import Region

from ..column_sets import ColumnSet, ColumnSetItem
from ..columns import Column
from ..filters import ModelChoicesFilter
from .base import Slit


class RegionSlit(Slit):
    name = "region"
    label = "Регионы"

    def get_queryset(self):
        return Region.objects.all()

    def get_filters(self):
        return [
            ModelChoicesFilter(
                "region",
                "id",
                "Регион",
                Region.objects.all(),
            ),
        ]

    def get_slit_key(self, data_source):
        return "education_org__region"

    def get_columns(self):
        return [Column("name", "Регион")]

    def get_columnsets(self):
        return [ColumnSet("region_info", "Регион", [ColumnSetItem("name")])]
