from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Status
from django.urls import reverse_lazy

from datetime import datetime

class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_status = Status.objects.get(name='published')
        context["post_list"] = Post.objects.filter(status=published_status).order_by("created_on").reverse()
        context["timestamp"] = datetime.now().strftime('%F %H:%M:%S')
        return context

class PostDraftListView(ListView):
    template_name = 'posts_list.html'  
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unpublished_status = Status.objects.get(name='unpublished')
        context["post_list"] = Post.objects.filter(
            status=unpublished_status).filter(
            author=self.request.user).order_by("created_on").reverse()
        context["timestamp"] = datetime.now().strftime('%F %H:%M:%S')
        return context

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name="posts/new.html"
    model = Post
    fields = ['title', 'subtitle', 'body', 'author', 'status']

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name="posts/edit.html"
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
