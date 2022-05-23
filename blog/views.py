from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post
from django.db.models import Q


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


class SearchResultsView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__icontains=query) |
            Q(tags__name__icontains=query) |
            Q(content__icontains=query)
        )
        return object_list
