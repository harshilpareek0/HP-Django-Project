from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.urls import reverse
# from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator
from django.db import models
from django.db.models import F

from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField(default = "Who Are You?")
    profile_pic = models.ImageField(null=True, blank = True, upload_to="images/profile/")
    date_of_birth = models.DateField(verbose_name=("Date of birth"), blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('index')
    #image = models.ImageField(default='x.jpg')   



# class CustomUser(AbstractUser):
#     display_name = models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_("Will be shown e.g. when commenting"))
#     date_of_birth = models.DateField(verbose_name=_("Date of birth"), blank=True, null=True)
#     address1 = models.CharField(verbose_name=_("Address line 1"), max_length=1024, blank=True, null=True)
#     address2 = models.CharField(verbose_name=_("Address line 2"), max_length=1024, blank=True, null=True)
#     zip_code = models.CharField(verbose_name=_("Postal Code"), max_length=12, blank=True, null=True)
#     city = models.CharField(verbose_name=_("City"), max_length=1024, blank=True, null=True)
#     #phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_("Enter a valid international mobile phone number starting with +(country code)"))
#     additional_information = models.CharField(verbose_name=_("Additional information"), max_length=4096, blank=True, null=True)
#     #photo = models.ImageField(verbose_name=_("Photo"), upload_to='photos/', default='photos/default-user-avatar.png')

#     class Meta:
#         ordering = ['last_name']

#     def __str__(self):
#         return f"{self.username}: {self.first_name} {self.last_name}"



# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
#     bio = models.TextField(max_length=500, blank=True)
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
class Exercise(models.Model):
    exerciser_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    exercise_name = models.CharField(max_length=200)
    def get_absolute_url(self):
        return reverse('progress')

class Posts(models.Model):
    post_number = models.IntegerField(default=0)
    post_maker = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_text = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    class Meta:
        ordering = [F('likes').desc(nulls_last=True)]
    def get_absolute_url(self):
        return reverse('forum')
    def __str__(self):
        return str(self.post_number)

class Replies(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="replies")
    reply_maker = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reply_text = models.CharField(max_length=1000)
    def get_absolute_url(self):
        return reverse('forum')