# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.shortcuts import render
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from tasks.models import Task
from teachers.models import Teacher
from tasks.serializers import TaskListSerializer, TaskDetailSerializer, TaskCreateSerializer

# Create your views here.


class TasksView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            teacher = user.teacher
            return list(set(teacher.managerTasks.all()).union(set(teacher.executorTasks.all())))
            #return Task.objects.filter(Q(managers__in=[teacher_id]) | Q(executors__in=[teacher_id])).distinct()
        else:
            return self.queryset


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        obj.begin_time = datetime.datetime.now().strftime("%Y-%m-%d")
        obj.save()


class TaskDestroyView(APIView):

    def delete(self, request):
        # @todo only managers can delete tasks
        task_ids = request.data.get("task_ids")
        Task.objects.filter(id__in=task_ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
