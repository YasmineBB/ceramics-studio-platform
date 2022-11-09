from django.contrib import admin
from .models import Post, Comment, UserProfile
from django_summernote.admin import SummernoteModelAdmin


"""
Class which allows the admin user to create, view and search for posts.
"""

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['caption', 'description']
    list_display = ['caption', 'status', 'created_on', 'user']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {"slug": ("caption",)}
    summernote_fields = ('description')


"""
Class which allows the admin user to view, search for, filter and approve comments on posts.
"""


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    search_fields = ['name', 'comment_body']
    list_display = ['name', 'comment_body', 'post', 'posted_on', 'approved']
    list_filter = ['approved', 'posted_on']
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'bio',]
    list_display = ['first_name', 'last_name', 'bio',]