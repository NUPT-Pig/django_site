from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, null=True)
    employee_id = models.CharField(max_length=6, default="000000")
    gender = models.BooleanField(default=False) #false->male true->female
    DEPARTMENT = (
        ('CS', 'Computer Science'),
        ('PHY', 'Physics'),
    )
    department = models.CharField(max_length=10, choices=DEPARTMENT, default='CS')
    POSITION = (
        ('TE', 'teacher'),
    )
    position = models.CharField(max_length=10, choices=POSITION, default='TE')
