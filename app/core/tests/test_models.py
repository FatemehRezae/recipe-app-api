"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'password123'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)

    def test_new_user_normalized_email(self):
        sample = [
            ['Test@example.com', 'Test@example.com'],
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@example.COM', 'test2@example.com'],
            ['test3@EXAMPLE.COM', 'test3@example.com']
        ]
        for email, expected in sample:
            user = get_user_model().objects.create_user(email=email, password='password123')
            self.assertEqual(user.email, expected)

    def test_new_user_emailess_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', password='45')
