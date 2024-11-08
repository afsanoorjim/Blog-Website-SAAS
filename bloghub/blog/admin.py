from django.contrib import admin
from . models import Blog

@admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    list_filter = ('author', 'publish_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish_date'