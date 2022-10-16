from django.urls import path
from .views import BlogHome
from .views import BlogPost

urlpatterns = [
    path('', BlogHome, name="blog-posts"),
    path('post/<int:primary_key>', BlogPost, name="blog-post"),
]
