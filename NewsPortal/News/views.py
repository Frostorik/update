from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostForm
from .filters import PostFilter
from django.shortcuts import redirect, get_object_or_404, render
from django.db import models
from datetime import datetime


class PostList(ListView):
    model = Post
    ordering = '-date_post'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 10


class PostSearch(ListView):
    model = Post
    ordering = '-date_post'
    template_name = 'flatpages/search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'new'


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_create.html'
    success_url = reverse_lazy('news')


class AddPost(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)


class PostEdit(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_edit.html'
    success_url = reverse_lazy('news')


class PostDelete(LoginRequiredMixin, DeleteView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_delete.html'
    success_url = reverse_lazy('news')


class CategoryList(ListView):
    model = Post
    template_name = 'categories/category_news.html'
    context_object_name = 'category_news'

    def get_queryset(self):
        self.category_post = get_object_or_404(Category, id=self.kwargs["pk"])
        queryset = Post.objects.filter(category_post=self.category_post).order_by("-date_post")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_not_subscriber"] = self.request.user
        context["category"] = self.category_post
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    message = "Вы были подписаны на рассылку новостей категории:"
    return render(request, "categories/subscribe.html", {"category": category, "message": message})
