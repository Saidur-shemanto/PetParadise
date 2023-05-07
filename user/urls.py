from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', 
        auth_views.LoginView.as_view(template_name='Login_page.html'), 
        name='login'),
    path('logout/', 
        auth_views.LogoutView.as_view(template_name='Petparadise_home.html'), 
        name='logout'),
    path('signup/', 
        views.Signup.as_view(), 
        name='signup'),
    path('profile/', 
        views.UserProfileView.as_view(), 
        name='user_Profile'),

]