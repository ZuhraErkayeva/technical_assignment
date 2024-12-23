from rest_framework import serializers
from .models import User, BlogPost, Comment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.id
        token['role'] = user.role
        return token


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['post','author','content','created_at']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class BlogPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ('id','title','content','is_published','author')

