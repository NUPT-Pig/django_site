# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TextFile(models.Model):
    name = models.CharField(max_length=64, default='default')
    file = models.FileField(upload_to='text/%Y/%m/%d', blank=True, null=True)


class MediaFile(models.Model):
    name = models.CharField(max_length=64, default='default')
    file = models.FileField(upload_to='media/%Y/%m/%d', blank=True, null=True)