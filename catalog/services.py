from django.core.cache import cache
from django.shortcuts import get_object_or_404

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получется данные по продуктам из кеша, или если кеш пуст дает из бд"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    """
    Сервисная функция для получения всех продуктов в указанной категории
    """
    category = get_object_or_404(Category, id=category_id)
    return Product.objects.filter(category=category)
