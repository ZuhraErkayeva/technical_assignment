from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import BlogPostPageNumberPagination, CommentLimitOffsetPagination

from .models import User,BlogPost,Comment
from .serializers import UserSerializers,BlogPostSerializers,CommentSerializer
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class BlogPostViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['created_at', 'updated_at']
    search_fields = ['^author__username', '=title']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['created_at']
    pagination_class = BlogPostPageNumberPagination



class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['created_at']
    search_fields = ['^author__username', '=post']
    ordering_fields = ['created_at']
    ordering = ['created_at']
    pagination_class = CommentLimitOffsetPagination


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)