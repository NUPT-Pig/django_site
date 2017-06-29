# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.test import TestCase, Client
from rest_framework import status

from common_interface import const

# Create your tests here.
class UploadTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.text = os.path.join(const.PathConst.LOG_FOLDER, 'general.log')
        self.text_upload_url = '/upload_files/text/upload/'
        self.text_list_url = '/upload_files/text/'

    def tearDown(self):
        pass

    def test_upload_txt(self):
        with open(self.text) as fp:
            response = self.client.post(self.text_upload_url, {'name': 'text', 'content': fp})
            self.assertEquals(response.status_code, status.HTTP_200_OK)

            response = self.client.get(self.text_list_url)
            self.assertEquals(response.status_code, status.HTTP_200_OK)
            print response.data
