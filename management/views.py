# -*- coding: utf-8 -*-
import logging

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from teachers.models import Teacher
from students.models import Student

from common_interface.log_interface import get_logger
logger = get_logger()

class LoginView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        #admin *****
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        logger.info('%s login' % username)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = Response(status=status.HTTP_200_OK)
            #if Teacher.objects.filter(user=user).exists():
            #    response.set_cookie('username', user.username, None, None, '/', None, False, False)
            #else:
            #    response.set_cookie('role', 'student', None, None, '/', None, True, False)
            #    response.set_cookie('role', user.student.id, None, None, '/', None, True, False)
            return response
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('random_string')
        return response


class RegisterView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        role = request.data.get('role', None)
        logger.info('%s register' % username)
        try:
            if User.objects.filter(username=username).exists():
                logger.error('%s already exist.' % username)
                return Response(status=status.HTTP_409_CONFLICT)
            user = User(username=username)
            user.set_password(password)
            user.save()
            if role == "teacher":
                Teacher.objects.create(user=user)
            elif role == "student":
                Student.objects.create(user=user)
        except Exception as e:
            print (e)

        return Response(status=status.HTTP_200_OK)
