from django.urls import path
from .views import HomeView, ContactsView, ProductDetailView, AddProductView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Страница контактов
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Детали продукта
    path('add_product/', AddProductView.as_view(), name='add_product'),  # Добавление продукта
]
