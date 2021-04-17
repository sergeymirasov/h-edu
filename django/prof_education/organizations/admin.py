from django.contrib import admin

from .models import EducationOrg


@admin.register(EducationOrg)
class EducationOrgAdmin(admin.ModelAdmin):
    pass
