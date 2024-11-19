from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import CustomUser,Book
from .forms import BookForm,CustomUserCreationForm
from .forms import ExampleForm
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace with your redirect
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Replace with your redirect
    return render(request, 'confirm_delete.html', {'book': book})

@permission_required('app_name.can_create', raise_exception=True)
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_user.html', {'form': form})

@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid:
            return redirect('success_view')
    else:
        form = ExampleForm()
    return render(request, 'form_example.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create your views here.
