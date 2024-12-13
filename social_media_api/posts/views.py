from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post,
        )
        return Response({'message': 'Post liked.'})
    return Response({'message': 'You have already liked this post.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post)

    if like.exists():
        like.delete()
        return Response({'message': 'Post unliked.'})
    return Response({'message': 'You have not liked this post.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = request.user.notifications.all().order_by('-timestamp')
    data = [
        {
            'actor': n.actor.username,
            'verb': n.verb,
            'timestamp': n.timestamp,
            'is_read': n.is_read
        }
        for n in notifications
    ]
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if created:
        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post,
        )
        return Response({'message': 'Post liked.'})
    return Response({'message': 'You have already liked this post.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post)
    
    if like.exists():
        like.delete()
        return Response({'message': 'Post unliked.'})
    return Response({'message': 'You have not liked this post.'})
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

def get_notifications(request):
    notifications = request.user.notifications.all().order_by('-timestamp')
    data = [{
        'actor': n.actor.username,
        'verb': n.verb,
        'timestamp': n.timestamp,
        'is_read': n.is_read
    } for n in notifications]
    return Response(data)

def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)
