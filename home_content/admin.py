from django.contrib import admin
from .models import AboutSection, Portfolio, Team

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'image')  # Display title, URL, and image in admin panel
    search_fields = ('title', 'url')  # Add search functionality based on title or URL
    list_filter = ('title',)  # Add filtering options by title

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')  # You can adjust what you want to display in the admin panel

