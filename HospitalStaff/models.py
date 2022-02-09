from statistics import mode
from tkinter import N
from django.db import models

# Create your models here.
class HospitalStaffDetails(models.Model):
    hospital_staff_id = models.IntegerField(null=False)
    hospital_staff_name = models.CharField(max_length=100, null=False)
    patient_id = models.IntegerField(null=False)

class AppointmentDetails(models.Model):
    appointment_id = models.IntegerField(null=False)
    start_dt_time = models.DateTimeField(null=False)
    end_dt_time = models.DateTimeField(null=False)
    doctor_id = models.IntegerField(null=False)
    patient_id = models.IntegerField(null=False)

class TransactionDetails(models.Model):
    transaction_id = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
    patient_id = models.IntegerField(null=False)
    transaction_info = models.CharField(max_length=100, null=False)
    transaction_status = models.CharField(max_length=100, null=False)
    receipt_info = models.CharField(max_length=100)