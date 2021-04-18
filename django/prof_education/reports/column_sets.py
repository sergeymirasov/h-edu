class ColumnSet:
    def __init__(self, key, label, items, auto=False):
        self.key = key
        self.label = label
        self.items = items
        self.auto = auto


class ColumnSetItem:
    def __init__(self, column_key, formats=None):
        self.column_key = column_key
        self.formats = formats or []


class ColumnFormats:
    emphasis = "emphasis"
