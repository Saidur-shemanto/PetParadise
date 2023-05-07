from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import userprofile

class UserCreateForm(UserCreationForm):
    user_image = forms.ImageField(required=False)
    user_contact = forms.CharField(max_length=30, required=False)
    birthdate = forms.DateTimeField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = userprofile
        fields = ('username', 'email', 'password1', 'password2', 'user_image', 'user_contact', 'birthdate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        self.fields['user_image'].label = 'Upload your image'
        self.fields['user_contact'].label = 'Contact'
        self.fields['birthdate'].label = 'Birthdate'

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     if commit:
    #         user.save()
    #         userprofile.objects.create(
    #             parent=user,
    #             user_image=self.cleaned_data.get('user_image'),
    #             user_contact=self.cleaned_data.get('user_contact'),
    #             birthdate=self.cleaned_data.get('birthdate')
    #         )
    #     return user