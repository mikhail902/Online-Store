from enum import UNIQUE

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(unique = True, max_length=35, blank=True, null=True, help_text="Введите номер телефона")
    country = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='users/avatars/',verbose_name="Аватар", blank=True, null=True, help_text="Вставте свое фото")
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    def __str__(self):
        return f"{self.phone_number}"
