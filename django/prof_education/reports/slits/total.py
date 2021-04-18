from .base import Line, LinesSlit


class TotalLine(Line):
    label = "Всего"


class TotalSlit(LinesSlit):
    name = "total"
    label = "Всего"

    def get_lines(self):
        return [TotalLine()]

    def get_filters(self):
        return []
