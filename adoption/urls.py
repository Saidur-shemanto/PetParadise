

from django.urls import path
from . import views

from .views import AdoptionPostListView
from django.conf import settings

app_name = 'adoptions'
urlpatterns = [
   
    path('', AdoptionPostListView.as_view(), name='adoption_post_list'),
    path('AdoptionpostCreate/', views.CreateAdoptPost.as_view(), name='adopt_post_create'),
    path('post/report/', views.reportAdoption.as_view(), name='report_adopt_post'),
    
]