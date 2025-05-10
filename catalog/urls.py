from django.urls import path
from .views import HomeView, ContactsView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Страница контактов
    path('products/', ProductListView.as_view(), name='product_list'),  # Список продуктов
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Детали продукта
    path('products/create/', ProductCreateView.as_view(), name='create_product'),  # Добавление продукта
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),  # Редактирование продукта
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),  # Удаление продукта
]