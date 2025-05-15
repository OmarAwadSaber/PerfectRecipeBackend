from django.contrib import admin
from django.urls import path
from .views import SearchView
urlpatterns = [
    path('recipes/', SearchView.as_view(), name='search-recipes'),
]