"""
URL mapping recipe
"""
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from recipe.views import RecipeViewSet

router=DefaultRouter()
router.register('recipes',RecipeViewSet,basename="recipes")

app_name="recipe"
urlpatterns=[
    path('',include(router.urls))
]