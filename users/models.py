from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150, unique=False, blank=True, null=True, verbose_name="username"
    )
    email = models.EmailField(
        unique=True, max_length=35, blank=True, null=True, help_text="Введите email"
    )
    phone_number = models.CharField(
        max_length=35, blank=True, null=True, help_text="Введите номер телефона"
    )
    country = models.CharField(max_length=20)
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Вставте свое фото",
    )

    token = models.CharField(
        max_length=100, verbose_name="token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"
