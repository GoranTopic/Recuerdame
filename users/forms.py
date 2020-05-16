from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from django_countries.fields import CountryField
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'country')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'country' , 'first_name', 'last_name', )

