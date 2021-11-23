from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class User(AbstractUser):

    objects = CustomUserManager()

    email = models.EmailField(verbose_name='e-mail', max_length=35, unique=True, blank=False, null=False)
    username = models.CharField(verbose_name='Имя в приложении', max_length=20, unique=True, blank=False, null=False)
    password = models.CharField(verbose_name='Пароль', max_length=128, blank=False, null=False)
    first_name = models.CharField(verbose_name='Имя', max_length=25)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    second_name = models.CharField(verbose_name='Отчество', max_length=25)
    created_at = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    avatar = models.FileField(null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} ({self.email})"



