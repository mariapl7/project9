from django.urls import path
from .views import register, login_view, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('edit_profile/', edit_profile, name='edit_profile'),  # URL для редактирования профиля
]

