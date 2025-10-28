from django.http import HttpResponse
from django.shortcuts import render


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
