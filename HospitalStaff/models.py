from django.db import models

# Create your models here.
class AppointmentDetails(models.Model):
    appointment_id = models.IntegerField(null=False)
    patient_id = models.IntegerField(null=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    appointment_with = models.CharField(max_length=255)
    requested_date = models.DateField(blank=True, null=True)
    status =models.CharField(max_length=255,default="Pending")

