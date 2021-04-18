from django.contrib import admin

from .models import Graduate


@admin.register(Graduate)
class GraduateAdmin(admin.ModelAdmin):
    pass
