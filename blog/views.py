from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from blog.serializers import PostSerializer

# Create your views here.

class PostAPIView(generics.CreateAPIView):
    queryset = Post
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, active=True)
        return Response(
            {"message":"Post success", "data":serializer.data},
            status=status.HTTP_200_OK
            )


"""
This view is for Reading the post specifically
"""
class ViewPostById(generics.RetrieveAPIView):
    queryset = Post
    serializer_class = PostSerializer
    
    def get(self, request, pk, *args, **kwargs):
        review = Post.objects.filter(id=pk).first()
        serializer = self.serializer_class(review)

        if review is not None:
            return Response(
                {"message": "Read Review", "data":serializer.data},
                status=status.HTTP_200_OK,
            )

"""This view is to edit the post"""
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "post_id"

    def put(self, request, pk):
        review = get_object_or_404(Post, id=pk)
        serializer = self.serializer_class(review, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(user=request.user, active=True)
            return Response(
                {"message": "Post updated", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Post update failed", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        product = Post.objects.all()
        serializer = self.serializer_class(product, many=True)
        return Response(
            {"message": "Recent post re", "data": serializer.data},
            status=status.HTTP_200_OK,
        )