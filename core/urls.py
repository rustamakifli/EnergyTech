from django.urls import path,re_path
from core.views import *
from django.contrib import admin
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add-applicant/', AddApplicant.as_view(), name='add_applicant'),
    path('check-promo-code/',check_promo_code,name="check-promo-code"),
    path('applicants/', HalfForm.as_view(), name='applicant_list'),
    path('edit-applicant/<int:pk>/', EditApplicantView.as_view(), name='edit_applicant'),
    path('completed-applicants/', FullForm.as_view(), name='applicant_list_fulled'),

]



