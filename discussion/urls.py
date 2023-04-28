from django.urls import path
from . import views
app_name = 'posts'
from .views import PostListView
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     # path('', views.PostList.as_view(), name = 'all'),
#     # path('new/', views.CreatePost.as_view(), name = 'create'),
#     # path('by/(?p<username>[-\w]+)', views.Userpost.as_view(), name = 'for_user'),
#     # path('by/(?p<username>[-\w]+)/(?p<pk>\d+)', views.PostDetail.as_view(), name = 'single'),
#     # path('delete/(?p<pk>\d+)', views.DeletePost.as_view(), name='view')
#     path('/posts/', views.PostList.as_view(), name = 'all'),
#     path('post/(?p<pk>\d+)'),
#     path('/postCreate/'views.PostList.as_view(), name = 'all'),
#     path('/postUpdate/(?p<pk>\d+)'),
#     path('/postDelete/(?p<pk>\d+)'),
    
# ]

urlpatterns = [
    # path('posts/', views.PostList.as_view(), name='all'),
    # path('post/<int:pk>/', views.PostDetail.as_view(), name='single'),
    path('', PostListView.as_view(), name='post_list'),
    path('postCreate/', views.CreatePost.as_view(), name='create'),
    # path('postUpdate/<int:pk>/', views.UpdatePost.as_view(), name='update'),
    # path('postDelete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)