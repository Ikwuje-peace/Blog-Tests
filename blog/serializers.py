from dataclasses import field
from pdb import post_mortem
from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =  ['title', 'author', 'body', 'pub_date']
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body', 'pub_date']