from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ProductForm


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
