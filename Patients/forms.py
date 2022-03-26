from django import forms
from django.forms import formset_factory
# from bootstrap_datepicker_plus import DatePickerInput

class appointmentForm(forms.Form):
    first_name = forms.CharField(label='Firstname.**', required=True,
                                   widget=forms.TextInput(attrs=
                                   {
                                       'required': True,
                                       'class': 'form-control',
                                       'placeholder': ('Firstname')
                                   }))
    last_name = forms.CharField(label='Lastname.**', required=True,
                                   widget=forms.TextInput(attrs=
                                   {
                                       'required': True,
                                       'class': 'form-control',
                                       'placeholder': ('Lastname')
                                   }))                               
    requested_date = forms.DateField(label="Requested Date", required=False,
                                     widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control', }))

    appointment_with = forms.IntegerField(label='Appointment with', required=True,
                                        widget=forms.NumberInput(attrs=
                                        {
                                            'required': False,
                                            'class': 'form-control',
                                            'placeholder': ('Appointment with')
                                        }))

class insuranceClaimRequestForm(forms.Form):
    patient_firstname = forms.CharField(label='Firstname.**', required=True,
                                   widget=forms.TextInput(attrs=
                                   {
                                       'required': True,
                                       'class': 'form-control',
                                       'placeholder': ('patient_firstname')
                                   }))
                                   
    patient_lastname = forms.CharField(label='Lastname.**', required=True,
                                   widget=forms.TextInput(attrs=
                                   {
                                       'required': True,
                                       'class': 'form-control',
                                       'placeholder': ('patient_lastname')
                                   }))                               
    

    insurance_name = forms.CharField(label='Insurance policy name', required=True,
                                        widget=forms.TextInput(attrs=
                                        {
                                            'required': True,
                                            'class': 'form-control',
                                            'placeholder': ('insurance_name')
                                        }), max_length=200)

    claim_amt = forms.IntegerField(label= 'Claim amount', required=True,
                                     widget=forms.NumberInput(attrs=
                                     {
                                         'required':True,
                                         'class': 'form-control',
                                         'placeholder': ('claim_amt')
                                     }))

    