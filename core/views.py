from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms import *
from django.urls import reverse_lazy
from core.models import *
import random

# Create your views here.
class AddApplicant(LoginRequiredMixin,CreateView):
    template_name = "applicant.html"
    form_class = AddApplicantForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        p = form.save()
        p.user = self.request.user
        # p.appeal_no = generate_client_code()
        # p.client_code = generate_client_code()
        # print(p.user)
        if p.name_company and p.voen_code and p.voen_activity and p.reyestr_num and p.registr_num and p.company_address and p.tm_number and p.tm_x_coordination and p.tm_y_coordination and p.length:
            p.is_complete = True
        else:
            p.is_complete = False
        p.save()
        return super().form_valid(form)
# def generate_client_code():
#     return ''.join([str(random.randint(0, 9)) for _ in range(10)])

class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.user.is_authenticated:
            promo_code = PromoCode.objects.filter(user=request.user, used=False).first()
            if promo_code:
                context['promo_code'] = promo_code
            else:
                context['promo_code'] = 'Promo kod istifadə edilib'
        return self.render_to_response(context)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def check_promo_code(request):
    if request.method == 'POST':
        promo_code_str = request.POST.get('promo_code')
        try:
            promo_code = PromoCode.objects.get(code=promo_code_str)
            print(promo_code_str)
            print('*******')
            print(promo_code)
            if promo_code.used:
                print('first')
                is_valid = False
                message = "Bu promo kod istifadə olunub."
            else:
                print('second')
                is_valid = True
                promo_code.used = True
                promo_code.save()
                message = "Təbriklər,Promo kod tətbiq oldu!"
        except PromoCode.DoesNotExist:
            is_valid = False
            message = "Yanlış Promo kod.Zəhmət olmasa doğru daxil edin"

        response_data = {'is_valid': is_valid, 'message': message}
        return JsonResponse(response_data)

class HalfForm(ListView):
    template_name = 'applicant_list.html'
    model = Applicant

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(HalfForm, self).get_context_data(**kwargs)
        carsList = Applicant.objects.filter(is_complete=False)
        print(carsList)
        context['app'] = carsList
        return context
class FullForm(ListView):
    template_name = 'applicant_list_full.html'
    model = Applicant

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(FullForm, self).get_context_data(**kwargs)
        carsList = Applicant.objects.filter(is_complete=True)
        print(carsList)
        context['app'] = carsList
        return context
class EditApplicantView(LoginRequiredMixin, UpdateView):
    template_name = 'update_applicant.html'
    form_class = UpdateApplicantForm
    success_url = reverse_lazy('')
    model = Applicant

    def get_object(self):
        return Applicant.objects.filter(id=self.kwargs['pk']).first()

    def form_valid(self, form):
        p = form.save(commit=False)
        p.user = self.request.user
        print(p.user)
        if p.name_company and p.voen_code and p.voen_activity and p.reyestr_num and p.registr_num and p.company_address and p.tm_number and p.tm_x_coordination and p.tm_y_coordination and p.length:
            p.is_complete = True
        else:
            p.is_complete = False
        p.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditApplicantView, self).get_context_data(**kwargs)
        cars = Applicant.objects.filter(id=self.kwargs['pk']).first()
        context['app'] = cars
        return context
    
def my_custom_view(request):
    return HttpResponse("Hello, world!")