from django import forms

class RequestApproved(forms.Form):
    request_id = forms.IntegerField(label='approve')