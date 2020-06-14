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
    epitafo = models.TextField(max_length=300, null=True, blank=False)

    #genral information
    biografia = models.TextField(max_length=10000)
    
    # Dates 
    fecha_de_nacimiento = models.DateField(null=True, blank=False)
    fecha_de_muerte = models.DateField(null=True, blank=False)
    
    # Country
    pais = CountryField( blank=True, multiple=True)

    # City
    #city = to be implemente

    # multi Value for timeline 
    # linea_de_timpo = -to be implemented-

    # Images 
    imagen_de_fondo = models.ImageField(null=True, blank=True, upload_to='covers/', default='defaults/cover.jpg' )
    #imagen_de_perfil = models.ImageField(null=True, blank=True, upload_to='profiles/',  default='defaults/profile.jpg' )
    imagen_de_perfil = ResizedImageField(null=True, blank=True, size=[1000, 1000], quality=100, crop=['middle', 'center'], upload_to='profiles/')

    # creation time
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)

    # user foreign keys 
    creado_por = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='manager')

    class Meta:
        permissions = (
                ('can add tribute' , 'can_add_tribute'),
                ('can_add_content', 'can add content'),
                ('can_view_content', 'can view content'),
                )

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


class Relation(models.Model):
    RELATIONS_EN = [ 
            ('Parent', 'Parent'),
            ('Parent', 'Father'),
            ('Parent', 'Mother'),
            ('Grandparent', 'Grandparent'),
            ('Grandparent', 'Grandfather'),
            ('Grandparent', 'Grandmother'),
            ('Sibling', 'Sibling'),
            ('Sibling', 'Sister'),
            ('Sibling', 'Brother'),
            ('Cousin', 'Cousin'),
            ('Significant_other', 'Significant_other'),
            ('Significant_other', 'Boyfriend'),
            ('Significant_other', 'Girlfriend'),
            ('Spouse', 'Spouse'),
            ('Spouse', 'Husband'),
            ('Spouse', 'Wife'),
            ('Friend', 'Friend'),
            ('Friend', 'Close-Friend'),
            ('Friend', 'Close-Friend'),
            ]
    
    RELATIONS_ES = [ 
            ('Padre', 'Padre'), 
            ('Madre', 'Madre'),
            ('Abuelo', 'Abuelo'), 
            ('Abuela', 'Abuela'),
            ('Hermano', 'Hermano'),
            ('Hermana', 'Hermana'),
            ('Primo', 'Primo'),
            ('Prima', 'Prima'), 
            ('Novio', 'Novio'), 
            ('Novia', 'Novia'), 
            ('Esposo', 'Esposo'),
            ('Esposa', 'Esposa'), 
            ('Amigo', 'Amigo'), 
            ('Amigo Cercano', 'Amigo Cercano'), 
            ]

    # Memorial to which the relation is made to
    memorial = models.ForeignKey(Memorial, on_delete=models.CASCADE, related_name='related_memorial')
    # User to which the relation is made with
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE, related_name='related_user')
    # Relation Name
    relation_name = models.CharField(max_length=100, choices=RELATIONS_ES)
    def __str__(self):
        return str(self.user) + "-- " + str(self.relation_name) + " --" + str(self.memorial)


class LifeEvent(models.Model):
    # memorial to which the picture is related to 
    memorial = models.ForeignKey(Memorial, on_delete=models.CASCADE, related_name='life_events')

    # picture field
    picture = models.ImageField(null=True, blank=True, upload_to='images/')

    # user who uploaded the picture
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    # Event date
    event_date = models.DateTimeField( blank=True)

    #short description of the 
    description = models.CharField(max_length=255, blank=True)

    # creation time
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.description 

    def get_absolute_url(self):
        return reverse('memorial_detail', kwargs={'pk': self.memorial.pk})


class Image(models.Model):

    # memorial to which the picture is related to 
    memorial = models.ForeignKey(Memorial, on_delete=models.CASCADE, related_name='images')

    # picture field
    file = models.ImageField(null=True, blank=True, upload_to='images/')

    # user who uploaded the picture
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    #short description of the 
    description = models.TextField(max_length=5000, blank=True)

    # creation time
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.file.name + " - " + self.description 

    def get_absolute_url(self):
        return reverse('memorial_detail', kwargs={'pk': self.memorial.pk})

