from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Category

@admin.register(Category)
class CategoryAdmin(ModelAdmin):

    list_display = (
        'id',
        'title',
        'slug',
        'youtube_playlist_id',
        'display_order',
        'is_active',
    )

    list_display_links = ('title',)
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle', 'youtube_playlist_id')

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_editable = (
        'display_order',
        'is_active',
        'youtube_playlist_id',
    )

    ordering = ('display_order',)