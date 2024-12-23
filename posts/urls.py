from .serializers import MyTokenObtainPairSerializer
from .views import UserViewSet,BlogPostViewSet,CommentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(serializer_class=MyTokenObtainPairSerializer), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
router = DefaultRouter()
router.register("user", UserViewSet),
router.register('posts', BlogPostViewSet),
router.register('comments', CommentViewSet),
urlpatterns += router.urls


