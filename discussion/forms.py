from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import post

from django import forms
from .models import post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('post_title', 'postText', 'post_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['post_title'].label = 'Post Title'
        self.fields['postText'].label = 'Write your post'
        self.fields['post_image'].label = 'Upload Image'

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['post_title', 'postText', 'post_image']


# class PostCreateForm(UserCreationForm):

#     class Meta:
#         fields = ('post_title', 'postText', 'Image')
#         model = post()

#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.fields['post_title'].label = 'Post Title'
#         self.fields['postText'].lebel = 'Write your post'
#         self.fields['postImage'].lebel = 'Upload Image'


# class PostUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = post
# 		fields = ['post_title', 'postText', 'Image']