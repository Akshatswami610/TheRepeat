import os
from uuid import uuid4
from django.db import models
from django.utils.text import slugify


def category_background_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    unique_id = uuid4().hex[:12]
    return f"backgrounds/{unique_id}{ext}"


def category_cover_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    unique_id = uuid4().hex[:12]
    return f"covers/{unique_id}{ext}"


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)

    background_img = models.ImageField( upload_to=category_background_path )
    cover_img = models.ImageField( upload_to=category_cover_path )

    youtube_playlist_id = models.CharField( max_length=100, blank=True, help_text="Enter the YouTube Music playlist ID" )

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["display_order", "id"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
