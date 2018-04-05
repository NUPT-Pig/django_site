from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher
from course.models import Course, Lesson


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  #  teachers = models.ManyToManyField(Teacher, blank=True)
    course = models.ManyToManyField(Course, blank=True)
    student_id = models.CharField(max_length=8, default="00000000")
    gender = models.BooleanField(default=False) #false->male true->female
    term = models.IntegerField(default=0)


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)