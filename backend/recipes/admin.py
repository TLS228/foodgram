from django.contrib import admin
from django.db.models import Count

from recipes.models import (
    Tag,
    Ingredient,
    Recipe,
    IngredientInRecipe,
    Favorite,
    ShoppingCart
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Администрирование тегов."""
    list_display = ('id', 'name', 'slug')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Управление ингредиентами."""
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


class IngredientsInline(admin.TabularInline):
    """Вложенные ингредиенты в рецептах."""
    model = IngredientInRecipe
    extra = 1
    min_num = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Администрирование рецептов."""
    inlines = [IngredientsInline]
    list_display = ('name', 'author', 'favorites_count')
    search_fields = ('name', 'author__username', 'author__email')
    list_filter = ('tags',)

    @admin.display(description='Добавлено в избранное')
    def favorites_count(self, obj):
        """Подсчёт добавлений рецепта в избранное."""
        return obj.favorites_total

    def get_queryset(self, request):
        """Добавление аннотации для подсчёта избранных."""
        qs = super().get_queryset(request)
        return qs.annotate(favorites_total=Count('favorites'))


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    """Управление ингредиентами в рецептах."""
    list_display = ('recipe', 'ingredient', 'amount')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Администрирование избранных рецептов."""
    list_display = ('user', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Администрирование корзины покупок."""
    list_display = ('user', 'recipe')
