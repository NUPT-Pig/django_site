from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    user = models.ForeignKey(User, null=True)
    gender = models.BooleanField(default=False) #false->male true->female
