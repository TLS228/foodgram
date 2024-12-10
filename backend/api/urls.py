from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    UserViewSet,
    TagViewSet,
    IngredientViewSet,
    RecipeViewSet,
)

# Создаем роутер
api = DefaultRouter()

# Регистрируем вьюсеты с нужными базовыми именами
api.register('users', UserViewSet, basename='user')
api.register('tags', TagViewSet, basename='tag')
api.register('ingredients', IngredientViewSet, basename='ingredient')
api.register('recipes', RecipeViewSet, basename='recipe')

# Определяем урлы
urlpatterns = [
    path('', include(api.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
