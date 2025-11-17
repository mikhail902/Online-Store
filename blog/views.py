from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm


class BlogPostListView(ListView):
    """Список блоговых записей с фильтрацией по публикации"""
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Фильтрация: выводим только опубликованные статьи"""
        return BlogPost.objects.filter(is_published=True).order_by('-created_at')


class BlogPostDetailView(DetailView):
    """Детальный просмотр статьи с увеличением счетчика просмотров"""
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        """Увеличение счетчика просмотров при открытии статьи"""
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    """Создание новой блоговой записи"""
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blog:post_list')


class BlogPostUpdateView(UpdateView):
    """Редактирование блоговой записи с перенаправлением на просмотр статьи"""
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'

    def get_success_url(self):
        """Перенаправление на просмотр отредактированной статьи"""
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    """Удаление блоговой записи"""
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')