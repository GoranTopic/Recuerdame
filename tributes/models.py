from django.db import models
from django.urls import include 
from django.contrib.auth import get_user_model
# Create your models here.

class Tribute(models.Model):
    # user who has written this 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tribute_user')
    # a quote
    quote = models.CharField(max_length=300, null=True, blank=True)
    # an anecdote
    anecdote = models.CharField(max_length=300, null=True, blank=True)
    # writting
    writting = models.CharField(max_length=300, null=True, blank=True)
    # an image
    image = models.ImageField(null=True, blank=True, upload_to='tributes/')
    # creation time
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)
    # likes count 
    likes_count = models.IntegerField(null=True, blank=False)
    # likes count 
    comments_count = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return self.writting

    def get_absolute_url(self):
        return reverse('tribute_detail', args=[str(self.id)])

class Comment(models.Model):
    # Foregn key for the tribute
    tribute = models.ForeignKey(Tribute, on_delete=models.CASCADE, related_name='comments')
    # comment text
    comment = models.CharField(max_length=500, null=True, blank=False) 
    # author 
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Like(models.Model):
     # author 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # Foregn key for the tribute
    tribute = models.ForeignKey(Tribute, on_delete=models.CASCADE, related_name='likes')



