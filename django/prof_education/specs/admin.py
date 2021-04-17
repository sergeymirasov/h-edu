from django.contrib import admin

from .models import Specialization, EducationDirection


class EducationDirectionInline(admin.TabularInline):
    model = EducationDirection


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    inlines = (EducationDirectionInline,)
