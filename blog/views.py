from blog.models import Post
from rest_framework import generics
from blog.serializers import PostSerializer,PostDetailSerializer

# Create your views here.

class PostAPIView(generics.CreateAPIView):
    queryset = Post
    serializer_class = PostSerializer
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post
    serializer_class = PostDetailSerializer
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post
    serializer_class = PostSerializer

