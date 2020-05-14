from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Memorial, Eulogy


class MemorialListView(ListView):
    model = Memorial
    template_name = 'memorialListView.html'

class MemorialDetailView(DetailView):
    model = Memorial
    template_name = 'memorialDetailView.html'

