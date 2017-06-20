from django.contrib.auth.models import User
from rest_framework import status

from django.test import TestCase, Client
from students.models import Student
from teachers.models import Teacher


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
        user = User.objects.create(username='teacher_student')
        teacher = Teacher.objects.create(user=user, gender=True)

        response = self.client.post('/students/', data={'username': 'test_0', 'password': 'test_0', 'teachers': [teacher.id]})
        student = User.objects.get(username='test_0').student

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.filter(user__username='test_0').count(), 1)
        self.assertEqual(student.teachers.all()[0].id, teacher.id)

        student.user.delete()
        student.delete()
        user.delete()
        teacher.delete()

    def test_delete_student(self):
        student = self.students.pop()
        id = student.id
        print id
        response = self.client.delete('/students/detail/'+str(id)+'/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.filter(id=id).count(), 0)
        self.assertEqual(User.objects.filter(student__id=id).count(), 0)


    def test_put_student(self):
        pass