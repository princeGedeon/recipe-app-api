"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_success(self):
        email="test@gmail.com"
        password="testpass123"
        name="prince"
        user=get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password
        )
        self.assertEqual(user.name, name)
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_emmail_normalized(self):
        """Test email normalized"""
        sample_emails= [
            ['test1@EXAMPLE.com',"test1@example.com"],
            ['Test2@Example.com', "Test2@example.com"],
            ['TEST3@EXAMPLE.COM', "TEST3@example.com"],
            ['Test4@Example.COM', "Test4@example.com"]
        ]

        for email,expected in sample_emails:
            user=get_user_model().objects.create_user(
                email=email,name=email.split('@')[0],
                password="test1234"
            )
            self.assertEqual(user.email,expected)

    def test_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='',name="test",password="blabla")

    def test_create_superuser(self):
        user=get_user_model().objects.create_superuser(
            email="test5@gmail.com",
            name="test",
            password="blablablabla"
        )

        self.assertTrue(user.is_admin)
        self.assertTrue(user.is_staff)