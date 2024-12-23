from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination

class BlogPostPageNumberPagination(PageNumberPagination):
    page_size = 10



class CommentLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

