from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_create(request):
    # логика для создания продукта
    pass

@login_required
def product_detail(request, pk):
    # логика для просмотра деталей продукта
    pass

@login_required
def product_update(request, pk):
    # логика для обновления продукта
    pass

@login_required
def product_delete(request, pk):
    # логика для удаления продукта
    pass
