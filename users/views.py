from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from catalog.models import Product
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.conf import settings
from .models import Product
from .forms import ProductForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            # Отправка приветственного письма
            send_mail(
                'Добро пожаловать!',
                'Спасибо за регистрацию на нашем сайте.',
                settings.EMAIL_HOST_USER,  # Используем почтовый ящик из настроек
                [user.email],
                fail_silently=False,
            )
            messages.success(request, 'Ваш аккаунт был создан! Вы можете войти в систему.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


class ProductForm:
    pass


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Убедитесь, что у вас есть соответствующий маршрут
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form})

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
    return render(request, 'myapp/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'myapp/product_confirm_delete.html', {'product': product})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Замените на имя вашего URL для домашней страницы
            else:
                messages.error(request, 'Неверные учетные данные.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Замените 'profile' на имя вашего URL для профиля
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'users/edit_profile.html', {'form': form})


class CreateView:
    pass


class UserRegisterView(CreateView):

    def form_valid(self, form):
        user = form.save()
        send_mail(
            'Добро пожаловать!',
            'Спасибо за регистрацию на нашем сайте.',
            settings.DEFAULT_FROM_EMAIL,  # Используйте почтовый ящик из настроек
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)
