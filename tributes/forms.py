from django import forms 
from .models import Tribute


class TributeForm( forms.ModelForm ):
    class Meta:
        model = Tribute
        fields  = ['quote', 'quote_author', 'anecdote', 'writting', 'cover_image']
