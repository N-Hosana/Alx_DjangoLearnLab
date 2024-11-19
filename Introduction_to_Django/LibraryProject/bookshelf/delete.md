retrieved_book.delete()
remaining_books = Book.objects.all()
print(remaining_books)
