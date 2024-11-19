# api/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    api.urls
    rest_framework.generics.ListAPIView
    path('books/', BookList.as_view(), name='book-list'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
