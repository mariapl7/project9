from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView


urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('post/new/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('post/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]