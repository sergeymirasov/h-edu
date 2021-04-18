from django.http import FileResponse
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics
from rest_framework.response import Response

from .data_sources import get_data_sources, get_data_sources_dict
from .models import SavedReport
from .renderers import ExcelRenderer, JsonRenderer
from .reports import Report
from .serializers import (
    ColumnSetSerializer,
    DataSourceSerializer,
    SavedReportSerializer,
    SlitSerializer,
)
from .slits import get_slits, get_slits_dict


class DataSourceListView(generics.GenericAPIView):
    """Возвращает список источников данных"""

    def get(self, request, *args, **kwargs):
        serializer = DataSourceSerializer(get_data_sources(), many=True)
        return Response(serializer.data)


class SlitListView(generics.GenericAPIView):
    """Возвращает список срезов"""

    def get(self, request, *args, **kwargs):
        serializer = SlitSerializer(get_slits(), many=True)
        return Response(serializer.data)


class ReportParamsView(generics.GenericAPIView):
    def get_slit(self):
        return get_slits_dict()[self.request.query_params["slit_name"]]

    def get_data_source(self):
        return get_data_sources_dict()[self.request.query_params["data_source_name"]]

    def get_report(self):
        return Report(self.get_data_source(), self.get_slit())

    def get_params(self):
        raise NotImplementedError

    @extend_schema(
        parameters=[OpenApiParameter("slit_name"), OpenApiParameter("data_source_name")]
    )
    def get(self, request, *args, **kwargs):
        return Response(self.get_params())


class FilterListView(ReportParamsView):
    """Возвращает список фильтров по заданным источнику данных и срезу"""

    def get_params(self):
        return [filter.get_json() for filter in self.get_report().get_filters()]


class ColumnsListView(ReportParamsView):
    """Возвращает список доступных колонок по заданным источнику данных и срезу"""

    def get_params(self):
        return [column.get_json() for column in self.get_report().get_visible_columns()]


class ColumnSetListView(ReportParamsView):
    """Возвращает список наборов колонок"""

    def get_params(self):
        serializer = ColumnSetSerializer(
            self.get_report().get_visible_columnsets(), many=True
        )
        return serializer.data


class ExportSavedReportView(SingleObjectMixin, View):
    """Выгружает сохраненный отчет в формате xlsx"""

    model = SavedReport

    def get(self, request, *args, **kwargs):
        saved_report = self.get_object()
        data = ExcelRenderer().render(saved_report)
        # data = io.BytesIO(data.read())
        return FileResponse(
            data,
            as_attachment=True,
            filename="report.xlsx",
        )


class JsonPreviewSavedReportView(generics.GenericAPIView):
    """Получает json превью отчета"""

    queryset = SavedReport.objects.all()

    def get(self, request, *args, **kwargs):
        saved_report = self.get_object()
        return Response(JsonRenderer().render(saved_report))


class SavedReportListCreateView(generics.ListCreateAPIView):
    """Список отчетов и создание отчета"""

    queryset = SavedReport.objects.filter(name__isnull=False)
    serializer_class = SavedReportSerializer


class SavedReportUpdateView(generics.RetrieveUpdateAPIView):
    """Обновление и получение отчета"""

    queryset = SavedReport.objects.all()
    serializer_class = SavedReportSerializer
