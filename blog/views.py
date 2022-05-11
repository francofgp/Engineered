from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post


class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    queryset = Post.objects.all()[:3]
    context_object_name = 'posts'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class BlogListView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
