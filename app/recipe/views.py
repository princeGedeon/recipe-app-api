from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from recipe.serializers import RecipeSerailizer

from core.models import Recipe
from rest_framework.permissions import IsAuthenticated

from recipe.serializers import RecipeDetailSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe API"""
    serializer_class = RecipeDetailSerializer
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')



    def get_serializer_class(self):
        if self.action=='list':
            return RecipeSerailizer

        return self.serializer_class