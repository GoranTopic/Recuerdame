from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 
from django_resized import ResizedImageField
from django_countries.fields import CountryField

# Create your models here.
class Memorial(models.Model):

    # name fields 
    nombre = models.CharField(max_length=100, null=True, blank=False)
    segundo_nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido  = models.CharField(max_length=100, null=True, blank=False)
    segundo_apellido  = models.CharField(max_length=100, null=True, blank=True)

    # Epitaph, the writting to engraved on tombs 
    epitafo = models.CharField(max_length=300, null=True, blank=False)

    #genral information
    biografia = models.TextField(max_length=10000)
    
    # Dates 
    fecha_de_nacimiento = models.DateField(null=True, blank=False)
    fecha_de_muerte = models.DateField(null=True, blank=False)
    
    # Country
    pais = CountryField( blank=True, multiple=True)

    # multi Value for timeline 
    # -to be implemented-

    # Images 
    imagen_de_fondo = models.ImageField(null=True, blank=True, upload_to='covers/', default='defaults/cover.jpg' )
    #imagen_de_perfil = models.ImageField(null=True, blank=True, upload_to='profiles/',  default='defaults/profile.jpg' )
    imagen_de_perfil = ResizedImageField(null=True, blank=True, size=[1000, 1000], quality=100, crop=['middle', 'center'], upload_to='profiles/')


    # use foreign keys 
    creado_por = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='manager')


    def get_full_name(self):
        ''' Get the full name by checking and using the names which have'''
        full_name = str(self.nombre)
        if self.segundo_nombre is not None:
            full_name += ' ' + str(self.segundo_nombre)
        if self.apellido is not None:
            full_name += ' ' + str(self.apellido)
        if self.segundo_apellido is not None:
            full_name += ' ' + str(self.segundo_apellido)
        return full_name

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('memorial_detail', args=[str(self.id)])
