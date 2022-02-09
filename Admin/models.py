from operator import mod
from statistics import mode
from tkinter import N
from django.db import models

# Create your models here.
class AdminDetails(models.Model):
    admin_id = models.IntegerField(null=False)
    admin_name = models.CharField(max_length=100, null=False)