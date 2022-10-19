from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import  APIClient
from rest_framework import status

CREATE_USER_URL=reverse('user:create')

def create_user(**params):
    """Create user"""
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):

    def setUp(self):
        self.client=APIClient()

    def test_crezte_user_sucess(self):
        """Creating user"""

        playload={
            "email":"test@example.com",
            "name":"test",
            "password":"testpass123"
        }
        res=self.client.post(CREATE_USER_URL,playload)

        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user=get_user_model().objects.get(email=playload['email'])
        self.assertTrue(user.check_password(playload['password']))
        self.assertNotIn('password',res.data)

    def test_user_with_exist_error(self):
        """test"""
        payload={
            "email":"test@exemple.com",
            "name":"test",
            "password":"pass1pass2pass4"
        }
        create_user(**payload)
        res=self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)


    def test_pass_too_short_error(self):
        playload={
            'email':"test@example.com",
            'name':"test",
            "password":"pw"
        }
        res=self.client.post(CREATE_USER_URL,playload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exist=get_user_model().objects.filter(
            email=playload['email']
        ).exists()
        self.assertFalse(user_exist)