from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_image = models.ImageField(upload_to='media/user_images/', null=  True)
    user_email = models.EmailField(null=True)
    user_contact = models.CharField(max_length=30)
    birthdate = models.DateTimeField(null=True)
    membership_stat = models.CharField(max_length=1, choices=membership_choice, default=member_normal)
    parent = models.OneToOneField(User, on_delete= models.CASCADE)
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name