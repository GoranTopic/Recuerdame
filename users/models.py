from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
# Create your models here.

class CustomUser(AbstractUser):
    country = CountryField(multiple=True, blank=True)   


