from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import permission_required


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)  # Создаем объект, но не сохраняем
            product.owner = request.user  # Устанавливаем владельца
            product.save()  # Сохраняем продукт в базе данных
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/product_form.html', {'form': form})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'catalog/product_confirm_delete.html', {'product': product})


class HomeView:
    pass


class ContactsView:
    pass


class ProductDetailView:
    pass


class AddProductView:
    pass


def product_list():
    return None


@permission_required('products.can_unpublish_product', raise_exception=True)
def unpublish_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.is_published = False
    product.save()
    return redirect('product_list')


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.owner != request.user and not request.user.has_perm('products.can_unpublish_product'):
        return redirect('product_list')  # Или вернуть ошибку 403

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.owner != request.user and not request.user.has_perm('products.can_unpublish_product'):
        return redirect('product_list')  # Или вернуть ошибку 403

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'confirm_delete.html', {'product': product})
