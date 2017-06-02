from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from students.models import Students
from students.serializers import StudentsSerializer, UserSerializer
# Create your views here.


class StudentsView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    def post(self, request, *args, **kwargs):
        print '*************'
        try:
            response = super(StudentsView, self).post(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                user_serializer = UserSerializer(data=request.DATA)
                if user_serializer.is_valid():
                    user_obj = user_serializer.save()
                    self.object.user = user_obj
                    self.object.save()
        except Exception as e:
            print str(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return response