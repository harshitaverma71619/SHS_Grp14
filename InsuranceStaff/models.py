from django.db import models

# Create your models here.
class InsuranceStaffDetails(models.Model):
    insurance_staff_id = models.IntegerField(null=False)
    insurance_staff_name = models.CharField(max_length=100, null=False)
    patient_id = models.IntegerField(null=False)
    insurance_name = models.CharField(max_length=100, null=False)
    claim_status = models.CharField(max_length=100, null=False)
    claim_amt = models.IntegerField(null=False)