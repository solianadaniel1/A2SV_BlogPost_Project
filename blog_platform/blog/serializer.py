from rest_framework import serializers
from blog.models import  Blog, BlogRating, Comment, Like


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at']


class BlogRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogRating
        fields = ['id', 'user', 'blog', 'rating_value']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'blog', 'content', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'blog', 'created_at']
