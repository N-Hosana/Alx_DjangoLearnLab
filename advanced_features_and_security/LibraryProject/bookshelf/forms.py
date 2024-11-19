from django import forms
from .models import Book,CustomUser

class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['title', 'author', 'publication_year']
class CustomUserCreationForm:
    class Meta:
        models=CustomUser
        fields = ['username','date_of_birth']

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Replace with the appropriate model
        fields = ['title', 'author', 'publication_year']
