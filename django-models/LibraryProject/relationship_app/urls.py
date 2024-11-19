from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # URL pattern for the function-based view
    path('books/', views.list_books, name='list_books'),

    # URL pattern for the class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # User authentication routes
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
