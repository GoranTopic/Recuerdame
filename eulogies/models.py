from django.db import models
from django.contrib.auth import get_user_model
from django.urls import include 
# Create your models here.


class Eulogy(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='author')

    memorial = models.ForeignKey('memorials.Memorial', on_delete=models.CASCADE, related_name='eulogy')
   
    quote = models.CharField(max_length= 200, null=True, blank=True) 

    anecdote = models.TextField(max_length = 300, null=True, blank=True)

    writting  = models.TextField(max_length = 300, null=True, blank=True)
    
    image =  models.ImageField(null=True, blank=True, db_index=True)


