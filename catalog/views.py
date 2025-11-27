from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)

from catalog.forms import ProductForm
from catalog.models import Product


class HomeView(TemplateView):
    """CBV для домашней страницы"""

    template_name = "home.html"


class ContactView(TemplateView):
    """CBV для страницы контактов"""

    template_name = "contact.html"


class FormView(TemplateView):
    """CBV для страницы контактов"""

    template_name = "product_form.html"


class ContactResponseView(View):
    """CBV для обработки формы контактов"""

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

    def get(self, request):
        return render(request, "contact.html")


class ProductListView(ListView):
    """CBV для списка продуктов"""

    model = Product
    template_name = "products_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    """CBV для детального просмотра продукта"""

    model = Product
    template_name = "single_display_product.html"
    context_object_name = "products"

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs["pk"])


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:create_product")


class ProductsUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:update_product")


class ProductsDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")
