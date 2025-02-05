from django.urls import path
from .views import HomeView, ContactsView, ProductDetailView, AddProductView
from .views import (
    product_list,
    product_create,
    product_update,
    product_delete,
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Страница контактов
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Детали продукта
    path('add_product/', AddProductView.as_view(), name='add_product'),  # Добавление продукта
    path('', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/update/<int:pk>/', product_update, name='product_update'),
    path('product/delete/<int:pk>/', product_delete, name='product_delete'),
]
