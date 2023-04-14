from django.contrib import admin
from typing import Sequence
from django.contrib import admin, messages
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter

from core.models import *

admin.site.register(Appealicant)
admin.site.register(AppealicantDay)
admin.site.register(Applicant)
admin.site.register(Region)
admin.site.register(CompanyCategory)

admin.site.register(PromoCode)



# scoreboard_site.register(models.Post)
# Register your models here.

