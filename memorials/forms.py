# post/forms.py

from django import forms
from .models import Memorial

FIELDS = ['first_name', 'second_first_name', 'last_name', 'second_last_name',
          'biography' , 'date_of_birth', 'date_of_passing', 'profile_image' ,
          'cover_image' ]


class MemorialForm(forms.ModelForm):
    class Meta:
        model = Memorial
        fields = FIELDS

