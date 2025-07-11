from django.urls import path
from .views import BlogPostListCreateView,BlogPostDetailView,github_webhook
from 

urlpatterns=[
    path('posts/',BlogPostListCreateView.as_view(),name='post-list'),
    path('posts/<int:pk>/',BlogPostDetailView.as_view(),name='post-details'),
    path('webhook',github_webhook,name="github-webhook"),

]