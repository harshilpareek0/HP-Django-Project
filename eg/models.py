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