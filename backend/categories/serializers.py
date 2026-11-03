from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'slug',
            'subtitle',
            'background_img',
            'cover_img',
            'display_order',
            'is_active',
        ]