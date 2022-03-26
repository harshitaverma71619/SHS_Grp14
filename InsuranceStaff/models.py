from django.db import models

# Create your models here.
class InsuranceClaimDetails(models.Model):
    patient_id = models.IntegerField(null=False)
    patient_firstname = models.CharField(max_length=100, null=False, default="fn")
    patient_lastname = models.CharField(max_length=100, null=False, default="ln")
    insurance_name = models.CharField(max_length=100, null=False)
    claim_status = models.CharField(max_length=100, null=False, default="Pending")
    claim_amt = models.IntegerField(null=False)