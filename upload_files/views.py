# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from upload_files.models import TextFile, MediaFile
from upload_files.serializers import TextFileSerializers, MediaFileSerializers
# Create your views here.


class UploadTextView(APIView):

    def post(self, request):
        text_instance = TextFile(name=request.data['name'], file=request.FILES['content'])
        text_instance.save()
        return Response(status=status.HTTP_200_OK)


class TextListView(generics.ListAPIView):

    serializer_class = TextFileSerializers
    queryset = TextFile.objects.all()


class UploadMediaView(APIView):

    def post(self, request):
        """
        the same method as text ;
        django receive file , if sizeof(file)<2.5, just read it into memory; else save it into /tmp/***, then save it
        into destination folder piece by piece.
        it seems django do it for me; but if user grows, try to use chunks
        :param request:
        :return:
        """
        media_instance = MediaFile(name=request.data['name'], file=request.FILES['content'])
        media_instance.save()
        return Response(status=status.HTTP_200_OK)

