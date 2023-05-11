from django.urls import path
from . import views
app_name = 'posts'
from .views import PostListView
from django.conf import settings

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('postCreate/', views.CreatePost.as_view(), name='create'),
    path('postDetail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('commentCreate/<int:pk>/', views.CreateComment.as_view(), name='comment_create'),
]