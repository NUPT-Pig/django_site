# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from upload_files.models import TextFile

# Create your views here.


class UploadTextView(APIView):

    def post(self, request):
        print request.FILES
        text_instance = TextFile(name=request.data['name'], file=request.FILES['content'])
        text_instance.save()
        return Response(status=status.HTTP_200_OK)

