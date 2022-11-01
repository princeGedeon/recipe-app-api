from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from  rest_framework.test import APIClient
from core.models import Recipe
from recipe.serializers import RecipeSerailizer,RecipeDetailSerializer

RECIPES_URL=reverse('recipe:recipes-list')

def detail_url(recipe_id):
    return reverse('recipe:recipes-detail',args=[recipe_id])




def create_recipe(user,**params):
    defaults={
        "title":"test test",
        "time_minutes":2,
        'price':Decimal('5.25'),
        'description':"blablbl",
        "link":"http://a.com/a.pdf"
    }

    defaults.update(params)
    recipe=Recipe.objects.create(user=user,**defaults)
    return recipe


class PublicRecipeAPITest(TestCase):
    def setUp(self):
        self.client=APIClient()

    def test_auth_required(self):
        res=self.client.get(RECIPES_URL)
        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)

class PrivateRecipeApitests(TestCase):
    """Test authenticated API request"""

    def setUp(self):
        self.client=APIClient()
        self.user=get_user_model().objects.create_user(
            email="user@example.com",
            name="user",
            password="testpass123"
        )

        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        create_recipe(user=self.user)
        create_recipe(user=self.user)
        res=self.client.get(RECIPES_URL)

        recipes=Recipe.objects.all().order_by('-id')
        serializer=RecipeSerailizer(recipes,many=True)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data,serializer.data)

    def test_recipe_list_limited_to_user(self):
        """Test list of recipes to authenticated user"""
        other_user=get_user_model().objects.create_user(
            email="other@gmail.com",
            name="other",
            password="otherpasstest"
        )
        create_recipe(user=other_user)
        create_recipe(user=self.user)
        res=self.client.get(RECIPES_URL)
        recipes=Recipe.objects.filter(user=self.user)
        serializer=RecipeSerailizer(recipes,many=True)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data,serializer.data)

    def test_get_recipe_detail(self):
        recipe=create_recipe(user=self.user)
        url=detail_url(recipe.id)
        res=self.client.get(url)

        serializer=RecipeDetailSerializer(recipe,context={'request':"request"})
        self.assertEqual(res.data,serializer.data)