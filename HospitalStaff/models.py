from django.db import models

# Create your models here.
class HospitalStaffDetails(models.Model):
    hospital_staff_id = models.IntegerField(null=False)
    hospital_staff_name = models.CharField(max_length=100, null=False)
    patient_id = models.IntegerField(null=False)