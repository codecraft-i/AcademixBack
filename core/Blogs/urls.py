from django.urls import path
from .views import BlogPostList, BlogPostDetail

urlpatterns = [
    path("blog/", BlogPostList.as_view(), name="blog-list"),
    path("blog/<slug:slug>/", BlogPostDetail.as_view(), name="blog-detail"),
]