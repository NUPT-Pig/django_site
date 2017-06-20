from django.shortcuts import render
from rest_framework import generics, status

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer


# Create your views here.
class TeachersView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer