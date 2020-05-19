from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 

# Create your models here.




class Memorial(models.Model):

    # name fields 
    first_name = models.CharField(max_length=200, null=True, blank=False)
    second_first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name  = models.CharField(max_length=200, null=True, blank=False)
    second_last_name  = models.CharField(max_length=200, null=True, blank=True)

    #genral information
    biography = models.TextField(max_length=10000)
    
    # Dates 
    date_of_birth = models.DateField(null=True, blank=False)
    date_of_passing = models.DateField(null=True, blank=False)
    
    # Images 
    cover_image = models.ImageField(null=True, blank=True, upload_to='covers/', default='defaults/cover.jpg' )
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/',  default='defaults/profile.jpg' )

    # use foreign keys 
    created_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='manager')


    def get_full_name(self):
        ''' Get the full name by checking and using the names which have'''
        full_name = str(self.first_name)
        if self.second_first_name is not None:
            full_name += ' ' + str(self.second_first_name)
        if self.last_name is not None:
            full_name += ' ' + str(self.last_name)
        if self.second_last_name is not None:
            full_name += ' ' + str(self.second_last_name)
        return full_name

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('memorial_detail', args=[str(self.id)])
