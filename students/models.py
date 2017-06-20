from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True)
    teachers = models.ManyToManyField(Teacher, null=True, blank=True)
    gender = models.BooleanField(default=False) #false->male true->female
