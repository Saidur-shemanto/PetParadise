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

from braces.views import SelectRelatedMixin
from . import models
from . import forms

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

# class PostList(SelectRelatedMixin, generic, ListView):
#     model = models.post
#     select_related = ('user')

# class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic, CreateView):
#     fields = ('postText')
#     model = models.post
    
#     def form_valid(self, form):
#         self.object = form.save(commit = False)
#         self.object.user = self.request.user
#         self.object.save()
#         return super().form_valid(form)
   

    # def as_view(self):
    #     query = 

# class Userpost(generic, ListView):
#     model = models.post
#     template_name = 'user_post_list.html'

#     def get_queryset(self):
#         try:
#             self.post_user = User.objects.prefetch_related('posts').get(username_iexact= self.kwargs.get('username'))
#         except User.DoesNotExist:
#             raise Http404
#         else:
#             return self.post_user.all() 
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post_user'] = self.post_user
#         return context 


# class PostDetail(SelectRelatedMixin, generic, DetailView):
#     model = models.post
#     select_related = ('user')
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user__username__iexact = self.kwargs.get('username'))
    

 
# class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic, DeleteView):
#     model = models.post
#     select_related = ('user')
#     success_url = reverse_lazy('posts:all')

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user_id = self.request.user.id)
#     def delete(self,*args,**kwargs):
#         messages.success(self.request, 'Post Deleted')
#         return super().delete(*args, **kwargs)