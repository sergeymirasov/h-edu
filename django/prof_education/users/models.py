from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class CommitteeMember(User):
    org = models.ForeignKey(
        "organizations.EducationOrg",
        verbose_name=_("Учебная организация"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Член приемной комиссии"
        verbose_name_plural = "Члены приемной комиссии"
