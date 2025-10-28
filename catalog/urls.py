from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import contact, home

app_name = CatalogConfig.name


urlpatterns = [
    path("home/", home, name="home"),
    path("contact/", contact, name="contact"),
]
