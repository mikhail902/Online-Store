from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import contact, home, product_list, single_display_product

app_name = CatalogConfig.name


urlpatterns = [
    path("home/", home, name="home"),
    path("contact/", contact, name="contact"),
    path("", product_list, name="product_list"),
    path("products/<int:pk>/", single_display_product, name="single_product"),
]
