from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.api.filters import IngredientFilter
from .serializers import RecipeSerializer, TagSerializer, IngredientSerializer
from recipes.models import Recipe, Tag, Ingredient
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        # Логика для добавления в избранное
        return Response({'status': 'added to favorites'})


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = IngredientFilter
    search_fields = ['name']
