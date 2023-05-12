from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
import markdown
from autoslug import AutoSlugField
from user.models import userprofile
# Create your models here.


class post(models.Model):
    post_title = models.CharField(max_length=50)
    postText = models.TextField()
    # postText_html = models.TextField(editable=False)
    # post_slug = models.SlugField(null = True)
    post_image = models.ImageField(upload_to='media/', null= True, blank=True)
    update_date = models.DateTimeField(auto_now=True, null = True)
    create_date = models.DateTimeField(null = True)
    # likes = models.PositiveIntegerField(default=0)  
    post_auth = models.ForeignKey(
        userprofile, on_delete=models.CASCADE,
        related_name= 'post_user'
    )
    def get_user(self):
        return self.post_auth.username

    def __str__(self) -> str:
        return self.post_title
    
#     def save(self, *args, **kwargs):
#         self.postText_html = markdown.markdown(self.postText)
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('posts:single', 
#                 kwargs = {'username': self.user.username, 
#                         'pk':self.pk})
#     class Meta:
#         ordering = ['-update_date']
#         unique_together = ['user', 'postText']


class post_comment(models.Model):
    commentText = models.TextField()
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(null = True)  
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(
        userprofile, on_delete=models.CASCADE
    )
    # def comment_user(self):
    #     obj = User.objects.get(pk=self.user.pk)
    #     return obj.username
