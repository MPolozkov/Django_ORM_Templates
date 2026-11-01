from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from catalog.forms import ContactForm
from catalog.models import Product


def home(request):
    """Главная страница: список всех товаров."""
    products = Product.objects.all()
    return render(request, "catalog/home.html", {"products": products})


def product_detail(request, pk):
    """Страница одного товара. Если товара с таким pk нет, вернётся 404."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, "catalog/product_detail.html", {"product": product})


def contacts(request):
    """Страница контактов с формой обратной связи."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(
                request, f"Спасибо, {contact.name}! Ваше сообщение отправлено."
            )
            # Перенаправление защищает от повторной отправки при обновлении страницы
            return redirect("catalog:contacts")
    else:
        form = ContactForm()
    return render(request, "catalog/contacts.html", {"form": form})
