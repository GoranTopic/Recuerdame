from django.urls import path, include 
from .views import signupView


urlpattern = [
        path('signup/', signupView.as_view(), name="signup"),
        ]

