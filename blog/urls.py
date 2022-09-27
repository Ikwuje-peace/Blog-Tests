from django.urls import path
from blog.views import PostAPIView, PostDetailView

urlpatterns = [
    path('', PostAPIView.as_view()),
    path('<int:pk>', PostDetailView.as_view()),
]
