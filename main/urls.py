from django.urls import path, include
from .views import (
    home, detail, posts)

urlpatterns = [
    path("", home, name="home"),
    path("detail/", detail, name="detail"),
    path("posts/", posts, name="posts"),
    path('tinymce/', include('tinymce.urls')),
]
