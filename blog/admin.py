from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    actions = ['approve_comments', 'undo_approval']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def undo_approval(self, request, queryset):
        queryset.update(approved=False)
