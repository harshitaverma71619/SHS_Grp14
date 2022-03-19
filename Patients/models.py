import imp
from django.db import models
from Doctors.models import DoctorDetails

# Create your models here.
class PatientDetails(models.Model):
    patient_id = models.IntegerField(default=0, null=False)
    patient_name = models.CharField(max_length=100, null=False)
    patient_age = models.IntegerField(null=False)
    patient_weight = models.CharField(max_length=100, null=False)
    patient_height = models.CharField(max_length=100, null=False)
    patient_address = models.CharField(max_length=1000, null=False)
    patient_phone_no = models.IntegerField(null=False)
    patient_email = models.EmailField(null=True)
    patient_disease = models.CharField(max_length=1000, null=False)
    doctor_id = models.ForeignKey(DoctorDetails, null=True, on_delete=models.SET_NULL)
    insurance_id = models.IntegerField(null=False)
    patient_diagnosis = models.CharField(max_length=1000, null=False)
    patient_reports = models.CharField(max_length=1000, null=False)
    patient_prescription = models.CharField(max_length=1000, null=False)
