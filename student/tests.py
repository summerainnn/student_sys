from django.test import TestCase, Client
from .models import Student


# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='test',
            sex=1,
            email='test@test.com',
            profession='code',
            qq='2222',
            phone='1234532',
        )

    def test_creat_and_sex_show(self):
        student = Student.objects.create(
            name='test2',
            sex=1,
            email='test2@test.com',
            profession='code',
            qq='33333',
            phone='222222222',
        )
        name = 'test'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='4444@test.com',
            profession='code',
            qq='44444',
            phone='15555555',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302:')

        response = client.get('/')
        # print('RESPONSE', response.content.decode('UTF-8'))
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain test_for_post')
