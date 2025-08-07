from django.db import models

# Create your models here.

from django.db import models
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(unique=True)
    cover_image = models.ImageField(upload_to="blog_covers/")
    created_at  = models.DateTimeField(auto_now_add=True)

    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BlogSection(models.Model):
    blog   = models.ForeignKey(
        BlogPost, related_name="sections", on_delete=models.CASCADE
    )
    heading = models.CharField("Section title", max_length=255)
    body    = RichTextField("Rich text content")   # <b>, <h2>, <ul> ...
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.blog.title} – {self.heading}"
