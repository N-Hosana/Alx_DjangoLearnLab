from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns displayed in the admin list view
    list_filter = ('publication_year', 'author')  # Filters for publication year and author
    search_fields = ('title', 'author')  # Search functionality for title and author


