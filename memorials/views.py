from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Memorial, Eulogy


class MemorialListView(ListView):
    model = Memorial
    template_name = 'memorial_list.html'

class MemorialDetailView(DetailView):
    model = Memorial
    template_name = 'memorial_detail.html'

