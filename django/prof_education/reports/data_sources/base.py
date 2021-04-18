from django.db import models
from django.db.models import Subquery
from django.db.models.functions import Coalesce


class DataSource:
    name = None
    label = None
    model = None

    def get_filters_dict(self):
        return {filter.key: filter for filter in self.get_filters()}

    def get_q_exprs(self, filter_data):
        return [
            self.get_filters_dict()[key].get_q_expr(data)
            for key, data in filter_data.items()
            if key in self.get_filters_dict().keys()
        ]

    def get_columns_labels(self):
        return [column.label for column in self.get_columns()]

    def get_annotation_exprs(self, queryset, filter_data):
        columns = self.get_columns()
        return {
            column.key: Coalesce(
                Subquery(column.get_annotation()),
                0,
                output_field=models.FloatField(),
            )
            for column in columns
        }

    def annotate_queryset(self, queryset, slit_key, filter_data):
        columns = self.get_columns()
        q_exprs = self.get_q_exprs(filter_data)
        for column in columns:
            queryset = queryset.annotate(
                **{
                    column.key: Coalesce(
                        Subquery(column.get_subquery(slit_key, q_exprs)),
                        0,
                        output_field=models.FloatField(),
                    )
                }
            )
        return queryset

    def get_columns_dict(self):
        return {column.key: column for column in self.get_columns()}

    def get_column_by_key(self, key):
        return self.get_columns_dict()[key]

    def get_column_query(self, column_key):
        for group in self.get_columns_query_groups():
            if column_key in group.column_keys:
                return group.query
        raise ValueError


class ColumnGroup:
    def __init__(self, key, query, column_keys):
        self.key = key
        self.query = query
        self.column_keys = column_keys
