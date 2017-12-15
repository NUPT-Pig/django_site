import logging

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

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
            response.set_cookie('random_string', '12345', None, None, '/', None, True, False)
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
        logger.info('%s register' % username)
        user = User(username=username)
        user.set_password(password)
        user.save()
