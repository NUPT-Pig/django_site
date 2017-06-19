from django.contrib.auth.models import User
from rest_framework import status

from django.test import TestCase, Client
from students.models import Student


# Create your tests here.
class StudentsTestCase(TestCase):

    def setUp(self):
        self.students = []
        self.client = Client()
        for i in range(0, 9):
            username = 'student_' + str(i)
            gender = True if i%2 == 0 else False
            self.create_student(username, gender)

    def tearDown(self):
        for student in self.students:
            student.user.delete()
            student.delete()

    def create_student(self, username, gender):
        user = User.objects.create(username=username)
        student = Student.objects.create(user=user, gender=gender)
        self.students.append(student)

    def delete_student(self, student):
        self.students.remove(student)
        student.user.delete()
        student.delete()

    def test_get_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.students))

    def test_post_student(self):
        response = self.client.post('/students/', data={'username': 'test_0', 'password': 'test_0'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        student = User.objects.get(username='test_0').student
        self.students.append(student)
        self.assertEqual(Student.objects.all().count(), len(self.students))

    def test_delete_student(self):
        response = self.client.delete('/students/')

    def test_put_student(self):
        pass