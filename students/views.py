from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from students.models import Student
from students.serializers import StudentSerializer, UserSerializer

from common_interface.log_interface import get_logger
logger = get_logger()

# Create your views here.


class StudentsView(generics.ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        try:
            logger.info('request = %s' % request.data)
            response = super(StudentsView, self).post(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user_obj = user_serializer.save()
                    Student.objects.filter(id=response.data['id']).update(user_id=user_obj.id)
                else:
                    logger.error('save user error %s' % user_serializer.errors)
        except Exception as e:
            logger.error('save student error %s' % str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return response


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        try:
            response = super(StudentDetailView, self).put(request, *args, **kwargs)
            obj = self.get_object()
            if response.status_code == status.HTTP_200_OK:
                user_serializer = UserSerializer(obj.user, data=request.data, partial=True)
                if user_serializer.is_valid():
                    user_serializer.save()
                else:
                    logger.error('save user error %s' % user_serializer.errors)
        except Exception as e:
            logger.error('modify student error %s' % str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return response

    def delete(self, request, *args, **kwargs):
        try:
            #delete student, then user will be deleted too.   onetoone field action
            response = super(StudentDetailView, self).delete(request, *args, **kwargs)
        except Exception as e:
            logger.error('delete student error %s' % str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return response