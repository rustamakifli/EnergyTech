from django.urls import path,re_path
from user.views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),

    path('register/', AccountRegistrationView.as_view(), name='register'),
]