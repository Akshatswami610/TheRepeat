from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField( max_length=120, unique=True, blank=True )
    subtitle = models.CharField(max_length=255, blank=True)
    background_img = models.ImageField(upload_to="categories/media/backgrounds/")
    cover_img = models.ImageField( upload_to="categories/media/covers/" )

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