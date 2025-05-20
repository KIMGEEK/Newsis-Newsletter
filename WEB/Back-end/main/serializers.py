from rest_framework import serializers
from .models import Post, User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['postname', 'mainphoto', 'contents']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'categories']