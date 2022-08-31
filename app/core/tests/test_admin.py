from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.test import Client


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model.object.create_superuser(
            email='admin@example.com',
            password='passWord123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model.object.create_user(
            email='user@example.com',
            password='pass123',
            name='Test User'
        )

    def test_users_list(self):
        url = reverse('admin:core_user_changelist')
        res = self.client(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
