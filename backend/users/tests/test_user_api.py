from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tailwind.models import User
from django.test import TestCase

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword", avatar="test_avatar.jpg")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("testpassword"))
        self.assertEqual(self.user.avatar, "test_avatar.jpg")