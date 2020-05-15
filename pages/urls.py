from django.urls import path, include
from .views import HomePageView, AboutPageView, ContactPageView


urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('quesoy/', AboutPageView.as_view(), name='quesoy'),
        path('contactame/', ContactPageView.as_view(), name='contactame'),
        ]
