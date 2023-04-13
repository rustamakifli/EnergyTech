from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# from core.models import *
from django.http import Http404

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView 
from django.views.generic import CreateView,TemplateView, UpdateView,View,ListView,DeleteView

from django.contrib.auth.views import LoginView
# from user.forms import  *

from django.views import generic

# from django.utils.encoding import force_str
# from django.utils.http import urlsafe_base64_decode
# from user.utils import account_activation_token

# from user.tasks import send_email_confirmation
from user.forms import BaseRegistrationForm
# Create your views here.
USER = get_user_model()

class AccountRegistrationView(generic.CreateView):
    """
        Account Register View if user is login
        Return to dashboard view
    """

    template_name = "register.html"
    # form_class = BaseRegistrationForm
    model = USER
    success_url = reverse_lazy("login")
    user = None

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)