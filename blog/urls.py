from django.urls import path
from .views import AboutPageView, HomePageView,BlogListView, BlogDetailView


urlpatterns = [
    path('post/', BlogListView.as_view(), name='post'),
    path('post/<str:slug>', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]