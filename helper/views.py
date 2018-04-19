# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from helper.models import Account
from helper.serializers import AccountSerializer, AccountDetailSerializer

# Create your views here.


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all().order_by("-date")
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except Exception as e:
            print (e)

    def create(self, request, *args, **kwargs):
        try:
            if request.user is None:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="no user provide")
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


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer


class AccountCheckView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer

    def patch(self, request, *args, **kwargs):
        if self.request.user.id not in [2, 3, 6]:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return self.partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if self.request.user.id == 6:
                instance.valid = True
                instance.save()
                return Response(status=status.HTTP_200_OK)
            check_list = json.loads(instance.check_list) if instance.check_list is not None else []
            if self.request.user.id not in check_list:
                check_list.append(self.request.user.id)
            instance.check_list = json.dumps(check_list)
            if len(check_list) == 2:
                instance.valid = True
            instance.save()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print (e)


class TestView(APIView):

    def post(self, request):
        print (request.data)
        return Response(status=status.HTTP_200_OK)