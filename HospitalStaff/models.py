from django.db import models

# Create your models here.
class AppointmentDetails(models.Model):
    appointment_id = models.IntegerField(null=False)
    patient_id = models.IntegerField(null=False)
    first_name = models.CharField(max_length=255,default="fn")
    last_name = models.CharField(max_length=255,default="ln")
    appointment_with = models.CharField(max_length=255,default="General Appointmemnt")
    requested_date = models.DateField(blank=True, null=True)
    status =models.CharField(max_length=255,default="Pending")

