from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from core.models import *
from core.utils.tools import PROMOCODE_ERRORS


class AddApplicantForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = Applicant
        fields = (
            'name_company',
            'voen_code',
            'voen_activity',
            'category',
            'appeal_no',
            'appealicant',
            'appleant_day',
            'region',
            'reyestr_num',
            'registr_num',
            'company_address',
            'tm_number',
            'tm_x_coordination',
            'tm_y_coordination',
            'length',
            'more',
            'captcha',
            'promo_code'
        )   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['appeal_no'].initial = generate_client_code()
        self.fields['appeal_no'].widget.attrs['readonly'] = True

        self.fields["region"].empty_label = None
        self.fields["category"].empty_label = None

        self.fields["appleant_day"].empty_label = None
        self.fields["appealicant"].empty_label = None

    def clean_promo_code(self):
        # This will be updated
        if self.instance and self.instance.promo_code:
            return self.instance.promo_code


        message = ""
        # request = current_request()
        from django.db.models import Q
        promo_code = self.cleaned_data.get("promo_code", None)

        if promo_code:   

            promo = PromoCode.objects.filter(
            Q(code=promo_code, used=False))

            if promo.exists():
                promo = promo.get_valid()

            else:
                message = PROMOCODE_ERRORS.get("not_exist_or_not_suitable")

            if message:
                raise forms.ValidationError(message, code="promo_code")
        
        return promo_code
import random

def generate_client_code():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])
class UpdateApplicantForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = Applicant
        fields = (
            'name_company',
            'voen_code',
            'voen_activity',
            'category',
            'appeal_no',
            'appealicant',
            'appleant_day',
            'region',
            'reyestr_num',
            'registr_num',
            'company_address',
            'tm_number',
            'tm_x_coordination',
            'tm_y_coordination',
            'length',
            'more',
            'captcha',
            'promo_code'
        )   