from django.db import models

# Create your models here.
class DoctorDetails(models.Model):
    doctor_id = models.IntegerField(default=0, null=False)
    doctor_name = models.CharField(max_length=1000, null=False)
    doctor_spec = models.CharField(max_length=1000, null=False)