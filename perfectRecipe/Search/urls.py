from django.contrib import admin
from django.urls import path
from .views import SearchRecipeListView
urlpatterns = [
    path('recipes/', SearchRecipeListView.as_view(), name='search-recipes'),
]