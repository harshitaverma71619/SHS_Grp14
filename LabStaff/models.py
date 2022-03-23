from statistics import mode
from django.db import models

# Create your models here.
class LabReports(models.Model):
    report_info = models.CharField(max_length=1000)
    doctor_id = models.IntegerField(null=False)
    patient_id = models.IntegerField(null=False)
    lab_staff_id = models.IntegerField(null=False)
    report_status = models.CharField(max_length=100)
    request_status = models.CharField(max_length=100, null=False, default="Pending")

    def getRequest(self):
        return {self.doctor_id, self.patient_id, self.request_status}
