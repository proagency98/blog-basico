from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'content', 'is_published')
        }),
        ('Metadatos', {
            'fields': (),
            'classes': ('collapse',)
        }),
    )