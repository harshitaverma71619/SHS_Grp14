from django.contrib import admin
from .models import AdminDetails, StaffDetails, TransactionDetails

# Register your models here.
admin.site.register(AdminDetails)
admin.site.register(StaffDetails)
admin.site.register(TransactionDetails)