import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangogitapi.settings")

import django

django.setup()

from django.core.management import call_command

from django.urls import reverse

from django.test import TestCase
from django.test import Client


class TestViews200(TestCase):

    def test_status_code_home_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_status_code_find_user_200(self):
        response = self.client.get(reverse('find_user'))
        self.assertEqual(response.status_code, 200)

    def test_status_code_user_profile_200(self):
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)

    def test_status_code_user_repository_200(self):
        response = self.client.get(reverse('user_repository'))
        self.assertEqual(response.status_code, 200)




