from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['caption', 'description']
    list_display = ['caption', 'status', 'created_on', 'user']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    search_fields = ['user', 'comment_body']
    list_display = ['user', 'comment_body', 'post', 'posted_on', 'approved']
    list_filter = ['approved', 'posted_on']
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)