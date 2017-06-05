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
        try:
            response = super(StudentsView, self).post(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user_obj = user_serializer.save()
                    Students.objects.filter(id=response.data['id']).update(user_id=user_obj.id)
                else:
                    print user_serializer.errors
        except Exception as e:
            print str(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return response