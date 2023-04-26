from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class post(models.Model):
    post_title = models.CharField(max_length=50)
    postText = models.TextField()
    post_slug = models.SlugField(null = True)
    post_image = models.ImageField(upload_to='media/post_images/', null= True)
    update_date = models.DateTimeField(auto_now=True, null = True)
    uploader = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    def uploader(self):
        obj = User.objects.get(pk=self.author.pk)
        return obj.username

    def __str__(self) -> str:
        return self.post_title
    

class post_comment(models.Model):
    commentText = models.TextField()
    update_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    def user(self):
        obj = User.objects.get(pk=self.author.pk)
        return obj.username
