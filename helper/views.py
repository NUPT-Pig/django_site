# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from helper.models import Account
from helper.serializers import AccountSerializer

# Create your views here.


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        try:
            obj = serializer.save()
            obj.user = self.request.user
            obj.save()
        except Exception as e:
            print (e)