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

    def get_queryset(self):
        teacher_name = self.request.query_params.get("teacher_name", None)
        print teacher_name
        if teacher_name is not None:
            return Teacher.objects.filter(user__username__contains=teacher_name)
        else:
            return self.queryset


class TeachersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer
