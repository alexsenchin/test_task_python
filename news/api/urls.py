from django.contrib import admin
from django.urls import path
from .views import PostListAPIView, PostCreateAPIView, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView


urlpatterns = [
    path('news-list', PostListAPIView.as_view(), name='news-list'),
    path('create/', PostCreateAPIView.as_view(), name='news-create'),
    path('<slug:link>/', PostDetailAPIView.as_view(), name='news-detail'),
    path('<slug:link>/edit/', PostUpdateAPIView.as_view(), name='news-update'),
    path('<slug:link>/delete/', PostDeleteAPIView.as_view(), name='news-delete'),
]