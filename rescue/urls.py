from django.urls import path
from . import views
app_name = 'rescues'
from django.conf import settings

urlpatterns = [

    path('', views.rescueListView.as_view(), name='rescue_list'),
    path('rescue_apply/', views.rescueApplyview.as_view(), name='rescue_apply'),
    path('rescue_post/', views.rescuePostView.as_view(), name='rescue_post'),

]