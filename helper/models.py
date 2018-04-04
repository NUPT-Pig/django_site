# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def set_path(instance, filename):
    return 'account/{0}/{1}_{2}'.format(instance.user.username, instance.id, filename)


class Account(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=False)
    money = models.FloatField(default=0)
    comment = models.TextField(default="no comment")
    date = models.DateField(null=True)
    valid = models.BooleanField(default=False)
    check_list = models.CharField(max_length=5, null=True)
    file = models.FileField(upload_to=set_path, blank=True, null=True)