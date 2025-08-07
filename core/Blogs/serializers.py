from rest_framework import serializers
from .models import BlogPost, BlogSection


class BlogSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = BlogSection
        fields = ("id", "heading", "body", "order")


class BlogPostSerializer(serializers.ModelSerializer):
    sections = BlogSectionSerializer(many=True, read_only=True)

    class Meta:
        model  = BlogPost
        fields = (
            "id",
            "title",
            "slug",
            "cover_image",
            "created_at",
            "sections",
            "is_popular"
        )
