from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, blank=True)
    gender = models.BooleanField(default=False) #false->male true->female
