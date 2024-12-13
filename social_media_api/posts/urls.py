from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.user_feed, name='user_feed'),
    path('posts/<int:pk>/like/', views.like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
    path('notifications/', views.get_notifications, name='get_notifications'),
]
