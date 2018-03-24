# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user = models.ForeignKey(User, null=True)
    money = models.FloatField(default=0)
    comment = models.TextField(default="no comment")
    valid = models.BooleanField(default=False)
    check_list = models.CharField(max_length=5, null=True)