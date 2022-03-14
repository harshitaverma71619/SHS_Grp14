from django.shortcuts import render
from django.views import View
from .forms import *

class patientHome(View):
    def get(self,request):
        return render(request,'patientHome.html',{
            'user':'aish'
        })

class bookAppointment(View):
    def get(self,request):
        return render(request,'bookAppointment.html',{
            'user':'aish',
            'appointmentForm':appointmentForm,
        })