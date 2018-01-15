from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=6, default="000000")
    gender = models.BooleanField(default=False) #false->male true->female
    DEPARTMENT = (
        ('UN', 'undefined'),
        ('CS', 'Computer Science'),
        ('PHY', 'Physics'),
    )
    department = models.CharField(max_length=10, choices=DEPARTMENT, default='UN')
    POSITION = (
        ('UN', 'undefined'),
        ('TE', 'teacher'),
    )
    position = models.CharField(max_length=10, choices=POSITION, default='UN')
    phone_number = models.CharField(max_length=11, default="")
    email = models.EmailField(default="")
