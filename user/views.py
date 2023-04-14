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
from user.forms import *
# Create your views here.
from core.models import PromoCode
import random
import string

USER = get_user_model()
def generate_promo_code():
    # Generate a 6 character random string for the promo code
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = MyUserLoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

@login_required
def logout(request):
    django_logout(request)
    return redirect('home')
class AccountRegistrationView(generic.CreateView):
    """
        Account Register View if user is login
        Return to dashboard view
    """

    template_name = "register.html"
    form_class = BaseRegistrationForm
    model = USER
    success_url = reverse_lazy("login")
    user = None

    def form_valid(self, form):
        user = form.save()
        promo_code = PromoCode.objects.create(user=user, code=generate_promo_code())
        user.save()
        if 'profile_picture' in self.request.FILES:
            user.profile_picture = self.request.FILES['profile_picture']
            print(user.profile_picture)
            user.save()
        return super().form_valid(form)