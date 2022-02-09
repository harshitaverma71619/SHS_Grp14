from ast import In
from re import L
from django.contrib import admin
from .models import LabStaffDetails, LabReports

# Register your models here.
admin.site.register(LabStaffDetails)
admin.site.register(LabReports)