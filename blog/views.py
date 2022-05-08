from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView,DetailView
from blog.models import Post


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogListView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


