# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskListSerializer, TaskDetailSerializer, TaskCreateSerializer

# Create your views here.


class TasksView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    def get_queryset(self):
        teacher_id = self.request.query_params.get("teacher_id", None)
        if teacher_id is not None:
            return Task.objects.filter(Q(managers__in=[3]) | Q(executors__in=[3])).distinct()
        else:
            return self.queryset


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def post(self, request, *args, **kwargs):
        print request.data
        return self.create(request, *args, **kwargs)


class TaskDestroyView(APIView):

    def delete(self, request):
        task_ids = request.data.get("task_ids")
        Task.objects.filter(id__in=task_ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer

