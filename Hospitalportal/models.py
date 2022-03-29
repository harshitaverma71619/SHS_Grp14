from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_email_verified=models.BooleanField(default=False)
    
class HospitalPortal(models.Model):
    Role = models.CharField(max_length=255,default="fn")
    username = models.CharField(max_length=255,default="ln")
    session = models.CharField(max_length=255,default="fn")
    
