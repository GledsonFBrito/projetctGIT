from django.test import TestCase
from django.test import Client


class TestHome(TestCase):
    def setUp(self):
        self.c = Client()

    def test_home(self):
        response = self.c.post('/')
        self.assertEqual(response.status_code, 200)

    def test_find_user(self):
        response = self.c.post('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page/home.html')

    def test_user_profile(self):
        response = self.c.post('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page/home.html')

    def test_user_repository(self):
        response = self.c.post('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page/home.html')
