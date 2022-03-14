from django import forms
from django.forms import formset_factory
# from bootstrap_datepicker_plus import DatePickerInput

class appointmentForm(forms.Form):
    firstname = forms.CharField(label='Firstname.**', required=True,
                                   widget=forms.TextInput(attrs=
                                   {
                                       'required': True,
                                       'class': 'form-control',
                                       'placeholder': ('Firstname')
                                   }))
    lastname = forms.CharField(label='Lastname.**', required=True,
                                   widget=forms.TextInput(attrs=
                                   {
                                       'required': True,
                                       'class': 'form-control',
                                       'placeholder': ('Lastname')
                                   }))                               
    requested_date = forms.DateField(label="Requested Date", required=False,
                                     widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control', }))

    appointment_with = forms.CharField(label='Appointment with', required=True,
                                        widget=forms.TextInput(attrs=
                                        {
                                            'required': False,
                                            'class': 'form-control',
                                            'placeholder': ('Appointment with')
                                        }), max_length=200)
    