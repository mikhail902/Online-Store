from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView, View)

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Category, Product
from catalog.services import get_product_from_cache, get_products_by_category


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

    def get_queryset(self):
        return get_product_from_cache()


class ProductDetailView(DetailView, LoginRequiredMixin):
    """CBV для детального просмотра продукта"""

    model = Product
    template_name = "single_display_product.html"
    context_object_name = "products"

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs["pk"])


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:create_product")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:update_product")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("user.can_unpublish_product") and user.has_perm(
            "user.delete_product"
        ):
            return ProductModeratorForm
        raise PermissionDenied

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return get_object_or_404(Product, pk=self.kwargs["pk"])
        raise HttpResponseForbidden


class ProductsDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return get_object_or_404(Product, pk=self.kwargs["pk"])
        raise HttpResponseForbidden


class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "products"


class CategoryProductsListView(DetailView):
    model = Category
    template_name = "category_products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()

        # Используем сервисную функцию
        products = get_products_by_category(category.id)

        context.update(
            {
                "products": products,
            }
        )
        return context
