from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    HomeView,
    ContactView,
    ProductListView,
    ProductDetailView,
    ContactResponseView,
    ProductCreateView,
    ProductsUpdateView,
    ProductsDeleteView
)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact/response/", ContactResponseView.as_view(), name="contact_response"),
    path("", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="single_product"),
    path("products/create", ProductCreateView.as_view(), name="create_product"),
    path("products/<int:pk>/update/", ProductsUpdateView.as_view(), name="update_product"),
    path("products/<int:pk>/delete/", ProductsDeleteView.as_view(), name="delete_product")
]
