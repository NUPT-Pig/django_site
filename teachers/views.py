from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer, TeacherDetailSerializer, TeachersSimpleSerializer


from common_interface.log_interface import get_logger
logger = get_logger()

# Create your views here.
class TeachersView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeachersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer


class MyDetailView(generics.RetrieveAPIView):
    serializer_class = TeacherDetailSerializer

    def get_object(self):
        return self.request.user.teacher


class TeachersCheckView(generics.ListAPIView):
    serializer_class = TeachersSimpleSerializer

    def get_queryset(self):
        teacher_name = self.request.query_params.get("teacher_name", None)
        if teacher_name is not None and teacher_name != '':
            return Teacher.objects.filter(user__username__contains=teacher_name)
        else:
            return []
