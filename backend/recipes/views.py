from django.shortcuts import redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse

from recipes.models import Recipe


def short_link_redirect(request: HttpRequest, short_code: str) -> HttpResponse:
    """Перенаправление на полную ссылку рецепта."""
    recipe = get_object_or_404(Recipe, short_code=short_code)
    full_url = request.build_absolute_uri(f'/recipes/{recipe.id}')
    return redirect(full_url)
