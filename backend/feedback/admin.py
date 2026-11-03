from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):

    list_display = ( 'id', 'name', 'email', 'created_at', )
    search_fields = ( 'name', 'email', 'message',)

    ordering = ('-created_at',)
    readonly_fields = ('created_at',)