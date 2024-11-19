from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
     # Displaying the fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Adding a filter by publication year
    list_filter = ('publication_year',)

    # Enabling search functionality for title and author fields
    search_fields = ('title', 'author')

# Registering the Book model with the customized admin class
admin.site.register(Book, BookAdmin)

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)
