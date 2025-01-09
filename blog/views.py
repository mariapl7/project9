from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import BlogPostForm  # Предполагается, что мы создадим форму для модели
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.urls import reverse
from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'

    def get_queryset(self):
        # Возвращаем только опубликованные статьи
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'

    def get_object(self, queryset=None):
        # Получаем объект статьи
        obj = super().get_object(queryset)
        # Увеличиваем счетчик просмотров
        obj.views += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blogpost_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'is_published']

    def get_success_url(self):
        # Перенаправляем на страницу просмотра статьи
        return reverse('blogpost_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')
