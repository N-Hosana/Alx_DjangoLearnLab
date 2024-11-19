from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from .models import Book, Library


# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based detail view for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'


def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'


# Role-based views

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/admin_view.html', {'libraries': libraries})


# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    library = request.user.userprofile.library
    books = library.books.all() if library else []
    return render(request, 'relationship_app/librarian_view.html', {'library': library, 'books': books})


# Member view
@user_passes_test(is_member)
def member_view(request):
    library = request.user.userprofile.library
    books = library.books.all() if library else []
    return render(request, 'relationship_app/member_view.html', {'library': library, 'books': books})
