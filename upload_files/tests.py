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

    def tearDown(self):
        pass

    def test_upload_txt(self):
        with open(self.text) as fp:
            response = self.client.post('/upload_files/text/', {'name': 'text', 'content': fp})
            self.assertEquals(response.status_code, status.HTTP_200_OK)
