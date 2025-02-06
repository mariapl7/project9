from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Убедитесь, что у вас есть соответствующий маршрут
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp/product_form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'myapp/product_confirm_delete.html', {'product': product})


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'page_obj'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all()


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html', {'success': False})

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Здесь можно добавить логику для обработки сообщения, например, отправка email
        return render(request, 'catalog/contacts.html', {'success': True})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class AddProductView(CreateView):
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('home')


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    login_url = 'login'  # Укажите URL для перенаправления, если пользователь не авторизован


class ProductCreateView(LoginRequiredMixin, CreateView):
    pass


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    pass


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    pass
