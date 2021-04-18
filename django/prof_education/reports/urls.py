from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [
    path("slits/", views.SlitListView.as_view(), name="slit_list"),
    path("data-sources/", views.DataSourceListView.as_view(), name="data_source_list"),
    path("filters/", views.FilterListView.as_view(), name="filter_list"),
    path("columns/", views.ColumnsListView.as_view(), name="column_list"),
    path("columnsets/", views.ColumnSetListView.as_view(), name="columnset_list"),
    path(
        "saved-reports/",
        views.SavedReportListCreateView.as_view(),
        name="saved_report_list",
    ),
    path(
        "saved-reports/<int:pk>/",
        views.SavedReportUpdateView.as_view(),
        name="saved_report_detail",
    ),
    path(
        "saved-reports/<int:pk>/export/",
        views.ExportSavedReportView.as_view(),
        name="saved_report_export",
    ),
    path(
        "saved-reports/<int:pk>/json-preview/",
        views.JsonPreviewSavedReportView.as_view(),
        name="saved_report_json_preview",
    ),
]
