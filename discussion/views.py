from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.views import generic
from .models import post, post_comment
from django.utils import timezone
from .forms import PostCreateForm, CommentForm
from django.shortcuts import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


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

class PostListView(ListView):
    model = post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    ordering = ['-create_date']


    

from django.shortcuts import redirect

class PostDetailView(DetailView):
    model = post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.comment_user = request.user
            comment.save()
            return redirect('post_detail', pk=self.object.pk)
        else:
            context = self.get_context_data(object=self.object, form=form)
            return self.render_to_response(context)
        
class CreateComment(LoginRequiredMixin, CreateView):
    model = post_comment
    form_class = CommentForm
    template_name = 'post/create_comment.html'
    success_url = None 

    def form_valid(self, form):
        form.instance.comment_user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.kwargs['pk']})

