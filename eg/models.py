from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date created")
    age = models.IntegerField()
    #image = models.ImageField(default='x.jpg')
    def get_absolute_url(self):
        return reverse('profile')   

    
