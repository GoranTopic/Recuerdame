from django import forms
from .models import Image, LifeEvent

class LifeEventForm(forms.ModelForm):
    class Meta:
        model = LifeEvent
        fields = ['picture', 'description', 'event_date',  ]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture', 'description', ]
