# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from teachers.models import Teacher

# Create your models here.


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=64, default='未命名')
    course_id = models.IntegerField(default=0)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, default='未命名')



