from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)

class userprofile(models.Model):
    member_normal = 'N'
    member_pending = 'P'
    member_verified = 'R'
    membership_choice = [
        (member_normal, 'Normal'),
        (member_pending, 'Pending'),
        (member_verified, 'Rescuer')
    ]

    user_image = models.ImageField(upload_to='media/user_images/', null=True)
    user_contact = models.CharField(max_length=30, null=True)
    birthdate = models.DateTimeField(null=True)
    membership_stat = models.CharField(max_length=1, choices=membership_choice, default=member_normal)
    parent = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.parent.username}'s Profile"

    def get_absolute_url(self):
        return f"/users/{self.parent.username}"

    
def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            userprofile.objects.create(parent=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
