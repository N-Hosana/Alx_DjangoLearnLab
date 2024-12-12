from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book

class BookAPITests(TestCase):
    def setUp(self):
        # Set up reusable test data
        self.client = APIClient()
        self.author = Author.objects.create(name="Test Author")
        self.book_data = {
            "title": "Test Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        self.book = Book.objects.create(
            title="Existing Book",
            publication_year=2020,
            author=self.author
        )

    def test_create_book(self):
        # Test creating a new book
        response = self.client.post("/api/books/", self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.book_data["title"])

    def test_get_books(self):
        # Test retrieving all books
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.book.title)

    def test_update_book(self):
        # Test updating an existing book
        updated_data = {"title": "Updated Book", "publication_year": 2023}
        response = self.client.put(f"/api/books/{self.book.id}/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], updated_data["title"])

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_create_book_invalid_year(self):
        # Test validation: Publication year cannot be in the future
        invalid_data = self.book_data.copy()
        invalid_data["publication_year"] = 3000  # Future year
        response = self.client.post("/api/books/", invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("publication_year", response.data)

    def test_unauthenticated_access(self):
        # Example: Ensure protected endpoints reject unauthenticated requests
        response = self.client.post("/api/books/", self.book_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
