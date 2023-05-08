from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import rescueApply, rescuePost
from .forms import rescueApplyform, rescuePostForm
from django.urls import reverse_lazy
from django.utils import timezone
# Create your views here.
class rescueApplyview(LoginRequiredMixin, CreateView):
    model = rescueApply
    form_class = rescueApplyform
    template_name = 'rescue/rescue_apply_form.html'
    success_url = reverse_lazy('rescues:rescue_list')

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        self.request.user.membership_stat = 'P'
        self.request.user.save()
        return super().form_valid(form)
    
class rescuePostView(LoginRequiredMixin, CreateView):
    model = rescuePost
    form_class = rescuePostForm
    template_name = 'rescue/rescue_post_form.html'
    success_url = reverse_lazy('rescues:rescue_list')

    def form_valid(self, form):
        form.instance.requester = self.request.user
        form.instance.create_date = timezone.now()
        return super().form_valid(form)
    
class rescueListView(ListView):
    model = rescuePost
    template_name = 'rescue/rescue_list.html'
    context_object_name = 'rescues'
    ordering = ['-create_date']