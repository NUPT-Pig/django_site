from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer, TeacherDetailSerializer


from common_interface.log_interface import get_logger
logger = get_logger()

# Create your views here.
class TeachersView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeachersDetailView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer
