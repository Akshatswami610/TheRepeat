from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    background_img = serializers.ImageField(read_only=True)
    cover_img = serializers.ImageField(read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'slug',
            'subtitle',
            'background_img',
            'cover_img',
            'youtube_playlist_id',
            'display_order',
            'is_active',
        ]