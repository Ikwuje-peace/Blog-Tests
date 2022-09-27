from django.urls import path
from blog.views import PostAPIView

urlpatterns = [
    path('', PostAPIView.as_view())
]
