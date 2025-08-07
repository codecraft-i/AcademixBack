from django.contrib import admin

# Register your models here.

# blog/admin.py
from django.contrib import admin
from .models import BlogPost, BlogSection
from django.contrib.admin import TabularInline

class BlogSectionInline(TabularInline):
    model  = BlogSection
    extra  = 1

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines             = [BlogSectionInline]
    list_display        = ("title", "created_at")
