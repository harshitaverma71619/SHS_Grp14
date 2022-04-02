from django import forms
from django.forms import formset_factory
# from bootstrap_datepicker_plus import DatePickerInput


class newInsurancePolicyForm(forms.Form):
    policy_name = forms.CharField(label='Policy Name', required=True,
                                   widget=forms.TextInput(attrs=
                                   {
                                       'required': True,
                                       'class': 'form-control',
                                       'placeholder': ('Policy Name')
                                   }))
    coverage_plans = forms.CharField(max_length = 200,label='Coverage Plans', required=True,
                                   widget = forms.Textarea(attrs=
                                   {
                                       'required': True,
                                       'class': 'form-control',
                                       'placeholder': ('Coverage Plans')
                                   }))                               
    insurance_amt = forms.IntegerField(label='Max Claim amount', required=True,
                                        widget=forms.NumberInput(attrs=
                                        {
                                            'required': True,
                                            'class': 'form-control',
                                            'placeholder': ('Max Claim amount')
                                        }))

