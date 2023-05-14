from django.db import models
from django.contrib.auth.models import User
from user.models import userprofile


# Create your models here.
class adoptionPost(models.Model):
    Not_adopted = 'NO'
    Adopted = 'YES'
    adoption_choice = [
        (Adopted, 'YES'),
        (Not_adopted, 'NO'),
       
    ]
    adoptText = models.TextField()
    adopt_image = models.ImageField(upload_to='media/', null= True, blank=True)
    update_date = models.DateTimeField(auto_now=True, null = True)
    create_date = models.DateTimeField(null = True)  
    adoptee = models.ForeignKey(
        userprofile, on_delete=models.CASCADE,
        related_name= 'adopt_user'
    )
    animalName = models.CharField(max_length=30)
    adoptee_contact = models.CharField(max_length=30, null=True)
    adoptee_location = models.TextField()
    adoptState = models.CharField(max_length=3, choices=adoption_choice, default=Not_adopted)


class adoptionReport(models.Model):
        Fake = 'F'
        Scam = 'S'
        Nudity = 'N'
        Hate_Speech = 'H'
        
        report_choice = [
        (Fake, 'Fake'),
        (Scam, 'Scam'),
        (Nudity, 'Nudity'),
        (Hate_Speech, 'Hate_speech'),
       
            ]
        report_date = models.DateTimeField(null = True)  
        reporter = models.ForeignKey(
        userprofile,
        on_delete=models.CASCADE,
        related_name='reporter_reports'
    )
        adoption_post = models.ForeignKey(
        adoptionPost,
        on_delete=models.CASCADE,
        related_name='reported_posts'
    )
        report_type = models.CharField(
        max_length=1,
        choices= report_choice,
        default= Fake
    )