from blog.models import Post
from rest_framework import generics
from blog.serializers import PostSerializer

# Create your views here.

class PostAPIView(generics.CreateAPIView):
    queryset = Post
    serializer_class = PostSerializer

