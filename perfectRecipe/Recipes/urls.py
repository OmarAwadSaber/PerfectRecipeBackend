from django.contrib import admin
from django.urls import path
from .views import RecipeListAPI, RecipeDetailAPI

urlpatterns = [
    path('', RecipeListAPI.as_view(), name='recipe-list'),
    path('<int:pk>/', RecipeDetailAPI.as_view(), name='recipe-detail'),
    path('ingredients/', RecipeListAPI.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', RecipeDetailAPI.as_view(), name='ingredient-detail'),
]