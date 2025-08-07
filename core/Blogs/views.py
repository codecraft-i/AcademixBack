from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostList(generics.ListCreateAPIView):
    queryset           = BlogPost.objects.prefetch_related("sections")
    serializer_class   = BlogPostSerializer
    lookup_field       = "slug"   # GET /api/blog/<slug>/

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = BlogPost.objects.prefetch_related("sections")
    serializer_class = BlogPostSerializer
    lookup_field     = "slug"
