from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import product_list, product_create, product_update, product_delete, product_detail


urlpatterns = [
    path('users/', include('users.urls')),
    path('', product_list, name='product_list'),  # Доступный для всех
    path('create/', product_create, name='product_create'),  # Только для авторизованных
    path('<int:pk>/', product_detail, name='product_detail'),  # Доступный для всех
    path('update/<int:pk>/', product_update, name='product_update'),  # Только для авторизованных
    path('delete/<int:pk>/', product_delete, name='product_delete'),  # Только для авторизованных
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
