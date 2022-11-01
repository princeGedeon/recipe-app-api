from rest_framework import serializers

from core.models import Recipe


class RecipeSerailizer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='recipe:recipes-detail')
    class Meta:
        model=Recipe
        fields=['id',"title","time_minutes","price","url"]
        read_only_fields=['id']

class RecipeDetailSerializer(serializers.ModelSerializer):
    """Extension du premier serializer"""

    class Meta:
        model = Recipe
        fields = ['id', "title", "time_minutes", "price", "link","description"]
        read_only_fields = ['id']
