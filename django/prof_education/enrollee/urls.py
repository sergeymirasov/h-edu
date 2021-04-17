from django.urls import path

from . import views

app_name = "enrollee"

urlpatterns = [
    path("", views.EnrolleeCreateView.as_view(), name="create"),
]
