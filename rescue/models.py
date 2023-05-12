from django.db import models
from django.contrib.auth.models import User
from user.models import userprofile

# Create your models here.
class rescuePost(models.Model):

    rescue_image = models.ImageField(upload_to='media/', null= True, blank=True)
    update_date = models.DateTimeField(auto_now=True, null = True)
    create_date = models.DateTimeField(null = True)  
    requester = models.ForeignKey(
        userprofile, on_delete=models.CASCADE,
        related_name= 'rescuereq_user'
    )
    animalName = models.CharField(max_length=30)
    requester_contact = models.CharField(max_length=30, null=True)
    rescue_location = models.TextField()
    animal_condition = models.CharField(max_length=3)

class rescueApply(models.Model):
    
    experience = models.IntegerField()
    applicant = models.ForeignKey(
        userprofile, on_delete=models.CASCADE,
        related_name= 'applicant_user'
    )
    def __str__(self) -> str:
        return self.applicant.username