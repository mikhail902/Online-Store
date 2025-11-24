from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name="Категория", help_text="Введите категорию продукта", max_length=50
    )
    description = models.CharField(
        max_length=100, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(verbose_name="Описание")
    pic = models.ImageField(
        upload_to="Product/pics.png",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Вставьте фото собаки",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        related_name="Products",
    )
    price = models.IntegerField(
        verbose_name="Цена продукта",
        help_text="Введите цену продукта",
        null=True,
        blank=True,
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name
