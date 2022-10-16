from xml.etree.ElementTree import Comment
from rest_framework import serializers
from news.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'link',
            'creation_date',
            'author_name',
            'amount_of_upvotes'
            ]

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'link',
            'author_name',
            ]

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        comment = Comment
        fields = [
            'title',
            'link',
            'creation_date',
            'author_name',
            'amount_of_upvotes',
            ]