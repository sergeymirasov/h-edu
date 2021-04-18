from django.db import models
from django.utils.translation import gettext as _

from .data_sources import get_data_sources_dict
from .reports import Report
from .slits import get_slits_dict


class SavedReport(models.Model):
    name = models.CharField(_("Название"), max_length=256, blank=True, null=True)
    data_source_name = models.CharField(_("Ключ источника данных"), max_length=128)
    slit_name = models.CharField(_("Ключ среза"), max_length=128)
    filters_data = models.JSONField(_("Информация по фильтрам"))
    columns_data = models.JSONField(_("Информация по колонкам"))

    class Meta:
        verbose_name = "Сохраненный отчет"
        verbose_name_plural = "Сохраненные отчеты"

    @property
    def data_source(self):
        return get_data_sources_dict()[self.data_source_name]

    @property
    def slit(self):
        return get_slits_dict()[self.slit_name]

    @property
    def report(self):
        return Report(self.data_source, self.slit)

    def generate(self):
        return self.report.generate(self.filters_data, self.columns_data)
