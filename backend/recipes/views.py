from django.shortcuts import redirect, get_object_or_404
from rest_framework import permissions, viewsets

from recipes.models import Recipe


class RedirectViewSet(viewsets.ViewSet):
    """Обработка коротких ссылок для рецептов."""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def short_link_redirect(self, request, short_code=None):
        """Перенаправление на полную ссылку рецепта."""
        recipe = get_object_or_404(Recipe, short_code=short_code)
        full_url = request.build_absolute_uri(f'/recipes/{recipe.id}')
        return redirect(full_url)
