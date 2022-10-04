from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['caption', 'description']
    list_display = ['caption', 'status', 'created_on']
    summernote_fields = ('description')

