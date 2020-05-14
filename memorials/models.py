from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Memorial(models.Model):

    first_name = models.CharField(max_length= 200, null=True, blank=False) 
    second_first_name = models.CharField(max_length= 200, null=True, blank=True) 
    last_name = models.CharField(max_length = 200, null=True, blank=False)
    second_last_name = models.CharField(max_length = 200, null=True, blank=True)

    biography = models.TextField(max_length = 300)

    date_of_birth = models.DateField(null=True, blank=True)
    date_of_passing = models.DateField(null=True, blank=True)

    cover_image = models.ImageField(null=True, blank=True, db_index=True)
    profile_image =  models.ImageField(null=True, blank=True, db_index=True)
    
    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='user')


    def get_full_name(self):
        return   ( str(self.first_name) 
                + ' ' + str(self.second_first_name) 
                + ' ' + str(self.last_name) 
                + ' ' + str(self.second_last_name) )

    def __str__(self):
        return self.get_full_name()

class Eulogy(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='author')

    memorial = models.ForeignKey(Memorial, on_delete=models.CASCADE, related_name='eulogy')
   
    quote = models.CharField(max_length= 200, null=True, blank=True) 

    anecdote = models.TextField(max_length = 300, null=True, blank=True)

    writting  = models.TextField(max_length = 300, null=True, blank=True)
    
    image =  models.ImageField(null=True, blank=True, db_index=True)


