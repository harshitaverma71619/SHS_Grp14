from urllib import request
from django import views
from django.shortcuts import render
from django.views import View

from LabStaff.models import LabReports

# Create your views here.
class labStaffHome(View):
    def get(self, request):
        return render(request, 'labStaffHome.html', {
            'user': 'Harshil'
        })

class viewRequests(View):
    def get(self, request):
        request_details = LabReports.objects.all()
        return render(request, 'viewRequests.html', {
            'requests': request_details
        })