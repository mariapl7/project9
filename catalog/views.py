from django.shortcuts import render, get_object_or_404, redirect
from .models import Product  # Импортируйте модель продукта
from .forms import ProductForm
from django.core.paginator import Paginator


def home(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 10)  # Показывать 10 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        success = True  # Успешная отправка данных

    return render(request, 'catalog/contacts.html', {'success': success})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Получите объект продукта или 404
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context)   # Замените на свой путь к шаблону


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправляем на главную страницу после сохранения
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})
