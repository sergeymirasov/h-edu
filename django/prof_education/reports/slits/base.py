from django.db import models
from django.db.models import F, Func, OuterRef, Subquery, Value

from ..column_sets import ColumnSet, ColumnSetItem
from ..columns import Column


class JsonBuildObject(Func):
    function = "jsonb_build_object"
    output_field = models.JSONField()


class Slit:
    name = None
    label = None

    def get_queryset(self):
        raise NotImplementedError

    def get_filters(self):
        raise NotImplementedError

    @property
    def filters_dict(self):
        return {filter.key: filter for filter in self.get_filters()}

    def get_filtered_queryset(self, filters_data):
        q_exprs = []
        for filter_key, filter_data in filters_data.items():
            if filter_key not in self.filters_dict:
                continue
            filter = self.filters_dict[filter_key]
            q_exprs.append(filter.get_q_expr(filter_data))
        return self.get_queryset().filter(*q_exprs)

    def get_filtered_data(self, filters_data):
        return self.get_filtered_queryset(filters_data)

    def get_slit_key(self, data_source):
        raise NotImplementedError

    def get_columns(self):
        raise NotImplementedError

    def get_columns_labels(self):
        return [column.label for column in self.get_columns()]

    def enrich_data(self, data, columns, q_exprs, data_source, columns_data):
        for column_group in data_source.get_columns_query_groups():
            json_build_args = []
            for column_key in column_group.column_keys:
                if column_key not in columns_data:
                    continue
                column = data_source.get_column_by_key(column_key)
                json_build_args.append(Value(column.key))
                json_build_args.append(column.annotation)
            query = (
                column_group.query.filter(*q_exprs)
                .filter(**{self.get_slit_key(data_source): OuterRef("pk")})
                .order_by()
                .values(self.get_slit_key(data_source))
            )
            query = query.annotate(
                **{column_group.key: JsonBuildObject(*json_build_args)}
            ).values(column_group.key)[:1]
            data = data.annotate(**{column_group.key: Subquery(query)})
            for column_key in column_group.column_keys:
                column = data_source.get_column_by_key(column_key)
                data = data.annotate(
                    **{column.key: F(f"{column_group.key}__{column.key}")}
                )
        return data


class Line:
    label = None

    def make_aggregations(self, queryset, aggregation_exprs):
        aggr = queryset.aggregate(**aggregation_exprs)
        for expr_key in aggregation_exprs.keys():
            setattr(expr_key, aggr[expr_key])

    def process_queryset(self, queryset):
        return queryset

    def enrich_data(self, columns, q_exprs, columns_data):
        for column in columns:
            orig_query = column.parent.get_column_query(column.key)
            if q_exprs:
                orig_query = orig_query.filter(*q_exprs)
            self.make_aggregation(
                self.process_queryset(orig_query),
                column.get_annotation(),
            )

    def make_aggregation(self, queryset, annotation):
        aggr = queryset.aggregate(**annotation)
        for expr_key in annotation.keys():
            setattr(self, expr_key, aggr[expr_key])


class LinesSlit(Slit):
    def get_lines(self):
        raise NotImplementedError

    def get_filtered_data(self, filters_data):
        return self.get_lines()

    def enrich_data(self, data, columns, q_exprs, data_source, columns_data):
        for line in data:
            line.enrich_data(columns, q_exprs, columns_data)
        return data

    def get_columns(self):
        return [Column("label", "", auto=True)]

    def get_columnsets(self):
        return [
            ColumnSet(
                "label",
                "",
                [
                    ColumnSetItem("label"),
                ],
                auto=True,
            )
        ]
