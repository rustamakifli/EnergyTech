from datetime import timezone

from django.conf import settings
from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models

from django.utils.translation import gettext_lazy as _

from django.utils import timezone
# from core.models import *
# Create your models here.

USER_MODEL = settings.AUTH_USER_MODEL

class MyUserManager(UserManager):


    def _create_user(self, email, password, **extra_fields):
        """
         Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
             raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class MyUser(AbstractUser):
    email = models.EmailField(_('Email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    father_name = models.CharField(_('Father name'),max_length=30,blank=True)
    phone = models.CharField(max_length=20, blank=True)
    home_phone = models.CharField(max_length=20, blank=True)

    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_images', null=True, blank=True, default='profile/default_pic.png'
    )

    gov_id = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Şəxsiyyət vəsiqəsinin nömrəsi"),
    )
    fin_code = models.CharField(
        db_index=True,
        blank=True,
        null=True,
        max_length=30,
        help_text=_("Şəxsiyyət fin kodu"),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    last_activity = models.DateTimeField(_("last activity"), blank=True, null=True)
    username = None
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "{full_name}".format(
            full_name=self.get_full_name(),
            email=self.get_username(),
        )

    def get_full_name(self):
        """
            Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
            Returns the short name for the user.
        """
        return self.first_name
