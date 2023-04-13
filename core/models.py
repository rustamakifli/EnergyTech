from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.
User = get_user_model()
# Create your models here.
class CompanyCategory(models.Model):
    category = models.CharField(
        _("Category name"),
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Şəxsi VÖEN"),
    )
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category

class Appealicant(models.Model):
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Appealicant"
        verbose_name_plural = "Appealicant"

    def __str__(self):
        return self.name

class AppealicantDay(models.Model):
    days = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Appealicant Day"
        verbose_name_plural = "Appealicant Days"

    def __str__(self):
        return self.days

class Region(models.Model):
    region = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.region

class Applicant(models.Model):
        #voen information
    user =models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_applicant')
    name_company = models.CharField(
        _("Müəssinin adı"),
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Müəssinin adı"),
    )
    voen_code = models.CharField(
        _("VÖEN Kod"),
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Şəxsi VÖEN"),
    )
    voen_activity = models.CharField(db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Fəaliyyət növü"),
    )
    #appleant information
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='company_category')
    appeal_no = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Müraciət No"),
    )
    appealicant = models.ForeignKey(Appealicant, on_delete=models.CASCADE, null=True, blank=True, related_name='appealicant_user')
    appleant_day = models.ForeignKey(AppealicantDay, on_delete=models.CASCADE, null=True, blank=True, related_name='appealicant_day_user')
    #object information
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, related_name='region_object')
    reyestr_num = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Reyestr number"),
    )
    registr_num = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Registration number"),
    )
    company_address = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Company Address"),
    )
    # tm
    tm_number = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("TM number"),
    )
    tm_x_coordination = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Tm X coordination"),
    )
    tm_y_coordination = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("TM y coordination"),
    )
    length = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Lentgh"),
    )
    more  = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=130,
        help_text=_("Add more"),
    )