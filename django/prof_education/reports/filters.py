from django.db.models import Q


class Filter:
    def __init__(self, key, field_name, label):
        self.key = key
        self.field_name = field_name
        self.label = label

    def get_json(self):
        raise NotImplementedError

    def get_q_expr(self):
        raise NotImplementedError


class NumberFilter(Filter):
    def get_json(self):
        return {"type": "number", "label": self.label, "key": self.key}

    def get_q_expr(self, data):
        expr = {}
        from_value = data.get("from")
        if from_value:
            expr[f"{self.field_name}__gte"] = from_value
        to_value = data.get("to")
        if to_value:
            expr[f"{self.field_name}__lte"] = to_value
        return Q(**expr)


class Choice:
    def __init__(self, value, label):
        self.value = value
        self.label = label

    def get_json(self):
        return {
            "value": self.value,
            "label": self.label,
        }


class ChoicesFilter(Filter):
    def __init__(self, key, field_name, label, choices):
        self.key = key
        self.field_name = field_name
        self.label = label
        self.choices = choices

    def get_json(self):
        return {
            "type": "choices",
            "key": self.key,
            "label": self.label,
            "choices": [choice.get_json() for choice in self.choices],
        }

    def get_q_expr(self, data):
        return Q(**{f"{self.field_name}__in": data})


class ModelChoicesFilter(ChoicesFilter):
    def __init__(self, key, field_name, label, queryset):
        self.key = key
        self.field_name = field_name
        self.label = label
        self.choices = [Choice(obj.id, str(obj)) for obj in queryset]
