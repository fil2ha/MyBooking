from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=255, verbose_name='Имя пользователя', unique=True)
    email = models.EmailField(verbose_name='Почта пользвотеля', unique=True, blank=True)
    password = models.CharField(verbose_name='Пароль пользователя')
    is_staff = models.BooleanField(verbose_name='Cтаф статус', default=False)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')


    def __str__(self):
        return self.username


    def get_absolute_url(self):
        return f'/profile/'