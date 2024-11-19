from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

rest_framework.generics.ListAPIView
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
