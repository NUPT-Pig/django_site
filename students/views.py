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


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

    def put(self, request, *args, **kwargs):
        try:
            response = super(StudentDetailView, self).put(request, *args, **kwargs)
            obj = self.get_object()
            if response.status_code == status.HTTP_200_OK:
                user_serializer = UserSerializer(obj.user, data=request.data, partial=True)
                if user_serializer.is_valid():
                    user_serializer.save()
                else:
                    print user_serializer.errors
        except Exception as e:
            print str(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return response

    def delete(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            if obj.user:
                obj.user.delete()
            response = super(StudentDetailView, self).delete(request, *args, **kwargs)
        except Exception as e:
            print str(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return response