"""
Tests for django admin
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTest(TestCase):
    """Test for Django odels"""
    def setUp(self):
        """Crer user and client"""
        self.client=Client()
        self.admin_user=get_user_model().objects.create_superuser(email="admin@gmail.com",name="test",password="testpasstest")
        self.client.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(
            email="user@example.com",
            name="user",
            password="testusertest"
        )

    def test_users_list(self):
        """Test user ar listed page"""
        url=reverse("admin:core_user_changelist")
        res=self.client.get(url)

        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)