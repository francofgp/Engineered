from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import AboutPageView, HomePageView, BlogListView, BlogDetailView


urlpatterns = [
    path('post/', BlogListView.as_view(), name='post'),
    path('post/<str:slug>', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
