from django.db import models
from django.contrib.auth.models import User

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
        User, on_delete=models.CASCADE,
        related_name= 'adopt_user'
    )
    animalName = models.CharField(max_length=30)
    adoptee_contact = models.CharField(max_length=30, null=True)
    adoptee_location = models.TextField()
    adoptState = models.CharField(max_length=3, choices=adoption_choice, default=Not_adopted)