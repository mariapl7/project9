from django.urls import path
from .views import HomeView, ContactsView, ProductDetailView, AddProductView
from .views import (
    product_list,
    product_create,
    product_update,
    product_delete,
)
from .views import CreateProductView, EditProductView, DeleteProductView, ProductListView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Страница контактов
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Детали продукта
    path('add_product/', AddProductView.as_view(), name='add_product'),  # Добавление продукта
    path('', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/update/<int:pk>/', product_update, name='product_update'),
    path('product/delete/<int:pk>/', product_delete, name='product_delete'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', CreateProductView.as_view(), name='create_product'),
    path('products/edit/<int:product_id>/', EditProductView.as_view(), name='edit_product'),
    path('products/delete/<int:product_id>/', DeleteProductView.as_view(), name='delete_product'),
]
