from django.contrib import admin

from .models import (
    Enrollee,
    EnrolleePassport,
    EnrolleeSpecialization,
    GraduatedInstitution,
    GosOlympiadStatus,
    WsrOlympiadStatus,
    AbylimpixStatus,
    SportAchievement,
    ParentData,
    EducationDoc,
)


class EnrolleeSpecializationInline(admin.TabularInline):
    model = EnrolleeSpecialization


class SportAchievementInline(admin.TabularInline):
    model = SportAchievement


@admin.register(Enrollee)
class EnrolleeAdmin(admin.ModelAdmin):
    inlines = (EnrolleeSpecializationInline, SportAchievementInline)


@admin.register(EnrolleePassport)
class EnrolleePassportAdmin(admin.ModelAdmin):
    pass


@admin.register(GraduatedInstitution)
class GraduatedInstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(GosOlympiadStatus)
class GosOlympiadStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(WsrOlympiadStatus)
class WsrOlympiadStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(AbylimpixStatus)
class AbylimpixStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(ParentData)
class ParentDataAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationDoc)
class EducationDocAdmin(admin.ModelAdmin):
    pass
