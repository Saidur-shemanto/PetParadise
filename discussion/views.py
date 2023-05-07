from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.views import generic
from .models import post, post_comment
from django.utils import timezone
from .forms import PostCreateForm, PostUpdateForm


from django.contrib.auth import get_user_model

User = get_user_model()

class CreatePost(LoginRequiredMixin, CreateView):
    model = post
    form_class = PostCreateForm
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('discussion:post_list')

    def form_valid(self, form):
        form.instance.post_auth = self.request.user
        form.instance.create_date = timezone.now()
        return super().form_valid(form)

def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostCreateForm()
    return render(request, 'post/post_form.html', {'form': form})

class PostListView(ListView):
    model = post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    ordering = ['-create_date']