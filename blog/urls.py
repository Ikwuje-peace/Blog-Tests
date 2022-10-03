from django.urls import path
from blog.views import PostAPIView, PostDetailView, PostUpdateAPIView

urlpatterns = [
    path('', PostAPIView.as_view()),
    path('<int:pk>', PostDetailView.as_view()),
    path('edit/<int:pk>/', PostUpdateAPIView.as_view()),

]
