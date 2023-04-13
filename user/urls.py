from django.urls import path,re_path
from user.views import *

urlpatterns = [
    path('register/', AccountRegistrationView.as_view(), name='register'),
]