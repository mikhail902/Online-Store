from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from catalog.models import Product


def home(request):
    return render(
        request,
        "home.html",
    )


def contact(request):
    return render(
        request,
        "contact.html",
    )


def response(request):
    if request.method == "POST":
        name = request.POST.get("name")
        massage = request.POST.get("massage")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contact.html")


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def single_display_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"products": product}
    return render(request, "single_display_product.html", context)
