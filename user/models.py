from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser 

class userprofile(AbstractUser):
    member_normal = 'N'
    member_pending = 'P'
    member_rescuer = 'R'
    membership_choice = [
        (member_normal, 'Normal'),
        (member_pending, 'Pending'),
        (member_rescuer, 'Rescuer')
    ]

    user_image = models.ImageField(upload_to='media/', null=True)
    user_contact = models.CharField(max_length=30, null=True)
    birthdate = models.DateTimeField(null=True)
    membership_stat = models.CharField(max_length=1, choices=membership_choice, default=member_normal)


    