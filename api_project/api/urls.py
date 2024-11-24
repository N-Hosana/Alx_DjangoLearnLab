
from django.urls import path, include
from .views import BookList,BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
api.urls
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]

#Generating Tokens
urlpatterns = [
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
