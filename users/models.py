from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
# Create your models here.

class CustomUser(AbstractUser):

    country = CountryField(multiple=True, blank=True)   

    profile_image = models.ImageField(blank=True, default='default/profile.jpg', upload_to='users/profiles')

