from rest_framework import serializers
from .models import Author, Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fiels = ['id','title','content','author','created_at']