from django.db.models import Case, Count, Value, When


def count_true(field_name):
    return count_value(field_name, True)


def count_value(field_name, value):
    return Count(Case(When(**{field_name: value, "then": Value(1)})))
