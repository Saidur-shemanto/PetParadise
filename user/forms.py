from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import userprofile

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].lebel = 'Email Address'


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = userprofile
		fields = ['first_name', 'last_name', 'user_image', 'user_contact']