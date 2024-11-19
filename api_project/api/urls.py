from django.contrib import admin
from django.urls import path, include  # Ensure `include` is imported
from .views import BookList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Ensure this line includes `api.urls`
    path('books/', BookList.as_view(), name='book-list'),
]
