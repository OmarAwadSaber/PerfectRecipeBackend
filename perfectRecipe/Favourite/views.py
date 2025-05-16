from django.shortcuts import render
from Recipes.models import Recipe
from rest_framework import generics
from Recipes.serializers import RecipeSerializer

# Create your views here.
class FavouriteView(generics.ListAPIView):
    queryset = Recipe.objects.filter(is_favourite=True)
    serializer_class = RecipeSerializer