from django import forms
from .models import Image, LifeEvent, Relation

class LifeEventForm(forms.ModelForm):
    class Meta:
        model = LifeEvent
        fields = ['picture', 'description', 'event_date',  ]

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', 'description', ]

class RelationForm(forms.ModelForm):
    class Meta:
        model = Relation
        fields = ['related_name']
