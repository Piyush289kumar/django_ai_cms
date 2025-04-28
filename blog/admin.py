from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'content')
    list_filter = ('published', 'created_at')
    
class CustomAdminClass(ModelAdmin):
    pass