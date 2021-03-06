# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from teachers.models import Teacher

# Create your models here.


class Task(models.Model):
    managers = models.ManyToManyField(Teacher, blank=True, related_name='managerTasks')
    executors = models.ManyToManyField(Teacher, blank=True, related_name='executorTasks')
    name = models.CharField(max_length=64, default="UNDEFINED")
    LEVEL = (
        (0, "normal"),
        (1, "middle"),
        (2, "important"),
    )
    level = models.IntegerField(choices=LEVEL, default=0)
    STATUS = (
        (0, 'executing'),
        (1, 'checking'),
        (2, 'finished'),
    )
    status = models.IntegerField(choices=STATUS, default=0)
    comment = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, auto_now_add=True)
    begin_time = models.DateField(null=True)
    finish_time = models.DateField(null=True)
    close_time = models.DateTimeField(null=True)
