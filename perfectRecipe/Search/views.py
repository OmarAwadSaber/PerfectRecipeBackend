from rest_framework import generics
from django.db.models import Q
from Recipes.models import Recipe
from Recipes.serializers import RecipeSerializer
class SearchView(generics.ListAPIView):
    serializer_class = RecipeSerializer
    def get_queryset(self):
        queryset = Recipe.objects.all()
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(ingredients__icontains=search_query)
            )
        return queryset
