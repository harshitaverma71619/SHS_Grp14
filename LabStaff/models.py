from django.db import models

# Create your models here.
class LabStaffDetails(models.Model):
    lab_staff_id = models.IntegerField(null=False)
    lab_staff_name = models.CharField(max_length=100, null=False)

class LabReports(models.Model):
    report_id = models.IntegerField(null=False)
    report_info = models.CharField(max_length=1000, null=False)
    doctor_id = models.IntegerField(null=False)
    patient_id = models.IntegerField(null=False)
    lab_staff_id = models.IntegerField(null=False)
    report_status = models.CharField(max_length=100, null=False)