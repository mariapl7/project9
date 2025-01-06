from django.urls import path
from . import views
from .views import product_detail


urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('contacts/', views.contacts, name='contacts'),  # Страница контактов
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
