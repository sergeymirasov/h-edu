from django.urls import path

from . import views

app_name = "specs"

urlpatterns = [
    path("", views.SpecializationListView.as_view(), name="list"),
]
