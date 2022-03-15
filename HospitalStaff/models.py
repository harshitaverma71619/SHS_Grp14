from django.db import models

# Create your models here.
class AppointmentDetails(models.Model):
    appointment_id = models.IntegerField(null=False)
    start_dt_time = models.DateTimeField(null=False)
    end_dt_time = models.DateTimeField(null=False)
    doctor_id = models.IntegerField(null=False)
    patient_id = models.IntegerField(null=False)