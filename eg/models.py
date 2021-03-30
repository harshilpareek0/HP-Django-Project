from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.urls import reverse
# from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator
from django.db import models
# from django.utils.translation import gettext_lazy as _

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date created")
    age = models.IntegerField()
    #image = models.ImageField(default='x.jpg')
    def get_absolute_url(self):
        return reverse('profile')   



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

