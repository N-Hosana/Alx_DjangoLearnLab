from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Set up reusable test data
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
        self.list_url = "/api/books/"

    def test_create_book(self):
        # Test creating a new book
        response = self.client.post(self.list_url, self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.book_data["title"])

    def test_get_books(self):
        # Test retrieving all books
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.book.title)

    def test_update_book(self):
        # Test updating an existing book
        detail_url = f"/api/books/{self.client.login}/"
        detail_url = f"/api/books/{self.book.id}/"
        updated_data = {"title": "Updated Book", "
     
