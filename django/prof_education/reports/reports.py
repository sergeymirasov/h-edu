from .column_sets import ColumnSet


class Report:
    def __init__(self, data_source, slit):
        self.data_source = data_source
        self.slit = slit

    def get_filters(self):
        return self.data_source.get_filters() + self.slit.get_filters()

    def get_columns(self):
        return self.data_source.get_columns() + self.slit.get_columns()

    def get_visible_columns(self):
        return [column for column in self.get_columns() if not column.auto]

    def get_columnsets(self):
        return self.slit.get_columnsets() + self.data_source.get_columnsets()

    def get_visible_columnsets(self):
        return [columnset for columnset in self.get_columnsets() if not columnset.auto]

    def get_column_by_key(self, key):
        for column in self.get_columns():
            if column.key == key:
                return column
        raise ValueError

    def get_usable_columnsets(self, columns_data):
        columnsets = []
        for columnset in self.get_columnsets():
            columnsets.append(
                ColumnSet(
                    columnset.key,
                    columnset.label,
                    [
                        item
                        for item in columnset.items
                        if item.column_key in columns_data
                        or self.get_column_by_key(item.column_key).auto
                    ],
                )
            )
        return [columnset for columnset in columnsets if len(columnset.items)]

    def get_ordered_columns(self, columns_data):
        columnsets = self.get_usable_columnsets(columns_data)
        res = []
        for columnset in columnsets:
            res += [item.column_key for item in columnset.items]
        return res

    def generate(self, filters_data, columns_data):
        data = self.slit.get_filtered_data(filters_data)
        data = self.slit.enrich_data(
            data,
            self.data_source.get_columns(),
            self.data_source.get_q_exprs(filters_data),
            self.data_source,
            columns_data,
        )

        columns = self.slit.get_columns() + self.data_source.get_columns()
        report_data = [
            {column.key: _col_value(item, column) for column in columns}
            for item in data
        ]
        ordered_columns = self.get_ordered_columns(columns_data)
        return [
            {key: report_line[key] for key in ordered_columns}
            for report_line in report_data
        ]


def _col_value(item, column):
    parts = column.key.split("__")
    current_val = item
    for part in parts:
        current_val = getattr(current_val, part)
    return column.render(current_val)
