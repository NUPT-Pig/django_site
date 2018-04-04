# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
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

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=json.loads(request.data.get('account_detail')))
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            print (e)

    def perform_create(self, serializer):
        try:
            obj = serializer.save()
            obj.user = self.request.user
            obj.file = self.request.FILES.get('img')
            obj.save()
        except Exception as e:
            print (e)


class TestView(APIView):

    def post(self, request):
        print (request.data)
        return Response(status=status.HTTP_200_OK)