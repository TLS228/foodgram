from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import Follow

# Получаем модель пользователя через get_user_model
User = get_user_model()


# Администрирование модели Follow
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Админка для подписок (Follow)."""
    list_display = ('user', 'author')
    search_fields = ('user__username', 'author__username')


# Настройка админки для модели User
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Кастомная админка для модели User."""
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    ordering = ('id',)


# Убираем модель Group из админки
admin.site.unregister(Group)
