from django.contrib import admin
from typing import Sequence
from django.contrib import admin, messages
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter

from user.models import (
    MyUser, 
)


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    readonly_fields = (
        "last_activity",
        'password',
    )
    search_fields = ("email", "first_name", "last_name")



