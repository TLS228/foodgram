from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    UserViewSet,
    TagViewSet,
    IngredientViewSet,
    RecipeViewSet,
)

# Создаем роутер
api_v1 = DefaultRouter()

# Регистрируем вьюсеты с нужными базовыми именами
api_v1.register('users', UserViewSet, basename='user')
api_v1.register('tags', TagViewSet, basename='tag')
api_v1.register('ingredients', IngredientViewSet, basename='ingredient')
api_v1.register('recipes', RecipeViewSet, basename='recipe')

# Определяем урлы
urlpatterns = [
    path('', include(api_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
