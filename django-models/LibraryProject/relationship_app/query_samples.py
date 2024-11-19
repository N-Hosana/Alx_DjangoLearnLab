from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian


# Example usage
if __name__ == "__main__":
    # Query all books by "J.K. Rowling"
    print("Books by J.K. Rowling:")
    for book in query_books_by_author("J.K. Rowling"):
        print(book.title)

    # List all books in "Central Library"
    print("\nBooks in Central Library:")
    for book in list_books_in_library("Central Library"):
        print(book.title)

    # Retrieve the librarian for "Central Library"
    print("\nLibrarian for Central Library:")
    librarian = retrieve_librarian_for_library("Central Library")
    print(librarian.name)
