from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django_resized import ResizedImageField
# Create your models here.

class CustomUser(AbstractUser):
    # country of user
    country = CountryField(multiple=True, blank=True)   
    # user Picture 
    imagen_image = ResizedImageField(null=True, blank=True, size=[500, 500], quality=100, crop=['middle', 'center'], upload_to='users/profile')
    # Bio


