from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Memorial
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.

# requiered field attibutes
FIELDS = ( 'nombre', 'segundo_nombre', 'apellido', 'segundo_apellido',
           'biografia' , 'fecha_de_nacimiento', 'fecha_de_muerte', 
           'imagen_de_perfil', 'image_de_fondo')


class MemorialListView(ListView):
    model = Memorial
    template_name = 'memorial_list.html'

class MemorialDetailView(DetailView):
    model = Memorial
    template_name = 'memorial_detail.html'

class MemorialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Memorial
    template_name = 'memorial_update.html'
    fields = FIELDS
    success_url = reverse_lazy('memorial_list')
    def test_func(self):
        ''' checks if the user is the same as the creator '''
        obj = self.get_object()
        return obj.creator == self.request.user

class MemorialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Memorial
    template_name = 'memorial_delete.html'
    fields = FIELDS
    success_url = reverse_lazy('memorial_list')
    def test_func(self):
        ''' checks if the user is the same as the creator '''
        obj = self.get_object()
        return obj.creator == self.request.user

class MemorialCreateView(LoginRequiredMixin, CreateView):
    model = Memorial
    template_name = 'memorial_new.html'
    fields = FIELDS
    login_url = 'login'
    
    def form_valid(self, form):
        ''' Set the user wich send the request as the form 'creator' '''
        print("Form valid RAN!!!")
        form.instance.creado_por = self.request.user
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Set the user wich send the request as the form 'creator' '''
        print("Form invalied RAN!!!")
        form.instance.creado_por = self.request.user
        form.instance.manager = self.request.user
        return super().form_valid(form)

