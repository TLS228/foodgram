from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models import F, Q, UniqueConstraint, CheckConstraint

from users.constans import MAX_EMAIL_LENGTH, MAX_USER_LENGTH


class Follow(models.Model):
    user = models.ForeignKey(
        'User',
        related_name='follower',
        on_delete=models.CASCADE,
        verbose_name='Кто подписан'
    )
    author = models.ForeignKey(
        'User',
        related_name='following',
        on_delete=models.CASCADE,
        verbose_name='На кого подписан'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            CheckConstraint(
                check=~Q(user=F('author')),
                name='no_self_follow'
            ),
            UniqueConstraint(
                fields=['user', 'author'],
                name='unique_follow'
            ),
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.author}'


class User(AbstractUser):
    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
        verbose_name='Электронная почта',
        help_text='Обязательное поле.'
    )
    username = models.CharField(
        max_length=MAX_USER_LENGTH,
        unique=True,
        verbose_name='Юзернейм',
        help_text='Обязательное поле.',
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': 'Пользователь с таким именем уже существует.',
        },
    )
    avatar = models.ImageField(
        upload_to='users',
        null=True,
        blank=True,
        verbose_name='Аватар',
    )
    first_name = models.CharField(
        max_length=MAX_USER_LENGTH,
        verbose_name='Имя',
        help_text='Обязательное поле.'
    )
    last_name = models.CharField(
        max_length=MAX_USER_LENGTH,
        verbose_name='Фамилия',
        help_text='Обязательное поле.'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    class Meta:
        ordering = ('username',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
