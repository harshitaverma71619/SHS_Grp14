from operator import mod
from statistics import mode
#from tkinter import N
from django.db import models

# Create your models here.
class AdminDetails(models.Model):
    admin_id = models.IntegerField(null=False)
    admin_name = models.CharField(max_length=100, null=False)

class StaffDetails(models.Model):
    staff_id = models.IntegerField(null=False)
    staff_name = models.CharField(max_length=100, null=False)
    staff_dept = models.CharField(max_length=100, null=False)

class TransactionDetails(models.Model):
    transaction_id = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
    patient_id = models.IntegerField(null=False)
    transaction_info = models.CharField(max_length=100, null=False)
    transaction_status = models.CharField(max_length=100, null=False)
    receipt_info = models.CharField(max_length=100)