from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

