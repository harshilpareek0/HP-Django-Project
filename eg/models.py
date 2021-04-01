from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

# class Profile(models.Model):
#     MALE = 'M'
#     FEMALE = 'F'
#     OTHER = 'O'

#     GENDER = [
#         (MALE, 'Male'),
#         (FEMALE,'Female'),
#         (OTHER, 'We respect your choices'),
#     ]

#     age = models.IntegerField(default = 0)
    
#     user_gender = models.CharField(
#         max_length=1,
#         choices=models.GENDER,
#         default=OTHER,
#     )

#     cardio = 'cardio'
#     weights = 'weight'
#     sports = 'sports'
#     calisthenics = 'calist'
#     none = 'none'

#     exChoices = [
#         (cardio, 'cardio'),
#         (weights, 'weights'),
#         (sports, 'sports'),
#         (calisthenics, 'calisthenics'),
#         (none, 'none'),
#     ]

#     user_exercises = models.CharField(
#         max_length = 6,
#         choices = models.exChoices,
#         default = none,
#     )
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date created")
    age = models.IntegerField()
    #image = models.ImageField(default='x.jpg')
    def get_absolute_url(self):
        return reverse('profile')   

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=200)
    def get_absolute_url(self):
        return reverse('progress')

class Posts(models.Model):
    post_text = models.CharField(max_length=1000)
    def get_absolute_url(self):
        return reverse('forum')