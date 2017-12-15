from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework import status

from teachers.models import Teacher

# Create your tests here.
class TeachersTestCase(TestCase):

    def setUp(self):
        self.teachers = []
        self.client = Client()
        for i in range(0, 3):
            username = 'teacher_' + str(i)
            gender = True if i % 2 == 0 else False
            self.create_teacher(username, gender)

    def create_teacher(self, username, gender):
        user = User.objects.create(username=username)
        teacher = Teacher.objects.create(user=user, gender=gender)
        self.teachers.append(teacher)

    def test_get_teachers(self):
        response = self.client.get('/teachers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.teachers))

