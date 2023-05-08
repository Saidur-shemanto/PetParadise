from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,  CreateView
from .models import adoptionPost
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import adoptionForm, adoptUpdateForm

User = get_user_model()

class CreateAdoptPost(LoginRequiredMixin, CreateView):
    model = adoptionPost
    form_class = adoptionForm
    template_name = 'adopt/adoption_form.html'
    success_url = reverse_lazy('adoptions:adoption_post_list')

    def form_valid(self, form):
        form.instance.adoptee = self.request.user
        form.instance.create_date = timezone.now()
        return super().form_valid(form)

def adoption_post_create(request):
    if request.method == 'POST':
        form = adoptionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('adoptions:post_detail', pk=post.pk)
    else:
        form = adoptionForm()
    return render(request, 'adopt/adoption_form.html', {'form': form})

class AdoptionPostListView(ListView):
    model = adoptionPost
    template_name = 'adopt/adoption_list.html'
    context_object_name = 'adoptions'
    ordering = ['-create_date']


