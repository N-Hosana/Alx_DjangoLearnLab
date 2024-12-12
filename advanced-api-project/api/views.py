
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from .models import Book
#Import a library to perform  the filtering
from django_filters import rest_framework
from rest_framework import DjangoFilterBackend
from rest_framework import filters 

#The purpose of this class is to List all available books.
class BookListView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

#Creating a class for retrieving a book by its ID

class BookDetailView(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


#Creating a class to add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

#Creating a class to update an existing book
class BookUpdateView(generics.UpdateAPIView):
     queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

#creating a class to remove a book
class BookDeleteView(generics.DestroyAPIView):
     queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]
