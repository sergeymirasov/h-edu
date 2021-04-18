class Column:
    def __init__(self, key, label, auto=False):
        self.key = key
        self.label = label
        self.auto = auto

    def get_json(self):
        return {"key": self.key, "label": self.label}

    def render(self, val):
        return val if val else ""


class AggrColumn(Column):
    def __init__(self, key, label, annotation, parent, auto=False):
        self.key = key
        self.label = label
        self.annotation = annotation
        self.parent = parent
        self.auto = auto

    def get_annotation(self):
        return {self.key: self.annotation}


class FloatMixin:
    def render(self, val):
        return "%.2f" % val if val else ""


class IntegerMixin:
    def render(self, val):
        return int(val) if val else ""


class FloatAggrColumn(FloatMixin, AggrColumn):
    pass


class IntegerAggrColumn(IntegerMixin, AggrColumn):
    pass
