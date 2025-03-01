from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from .forms import ProductForm
from django.contrib.auth.decorators import permission_required
from django.core.cache import cache
from django.shortcuts import render
from .services import get_products_by_category


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'create_product.html'
    fields = ['name', 'description', 'price', 'image', 'category', 'status']
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем владельца
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'edit_product.html'
    fields = ['name', 'description', 'price', 'image', 'category', 'status']
    success_url = reverse_lazy('product_list')

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user or self.request.user.has_perm('products.can_unpublish_product')


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user or self.request.user.has_perm('products.can_unpublish_product')


@permission_required('products.can_unpublish_product', raise_exception=True)
def unpublish_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.is_published = False
    product.save()
    return redirect('product_list')


class HomeView:
    pass

def product_detail(request, product_id):
    cache_key = f'product_{product_id}'
    product = cache.get(cache_key)

    if not product:
        product = get_object_or_404(Product, id=product_id)
        cache.set(cache_key, product, timeout=60*15)  # Кешировать на 15 минут

    return render(request, 'product_detail.html', {'product': product})


def products_by_category(request, category_id):
    products = get_products_by_category(category_id)
    return render(request, 'products/products_by_category.html', {'products': products})
