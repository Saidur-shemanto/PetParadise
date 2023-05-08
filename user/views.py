from django.views.generic import CreateView, UpdateView, View
from . import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import userprofile
from django.shortcuts import render, redirect
class Signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup_page.html'

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from .models import userprofile

User = get_user_model()

class UserProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user