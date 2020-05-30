from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Tribute
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.

# requiered field attibutes
FIELDS = ('quote', 'anecdote', 'writting', 'image')


class TributeListView(ListView):
    model = Tribute
    template_name = 'tribute_list.html'

class TributeDetailView(DetailView):
    model = Tribute
    template_name = 'tribute_detail.html'

class TributeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tribute
    template_name = 'tribute_update.html'
    fields = FIELDS
    login_url = 'login'
    success_url = reverse_lazy('tribute_list')
    def test_func(self):
        ''' checks if the user is the same as the creator '''
        obj = self.get_object()
        return obj.user == self.request.user

    def get_absolute_url(self):
        return reverse('memorial_detail', args=[str(self.id)])

class TributeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tribute
    template_name = 'tribute_delete.html'
    fields = FIELDS
    success_url = reverse_lazy('tribute_list')
    def test_func(self):
        ''' checks if the user is the same as the creator '''
        obj = self.get_object()
        return obj.creator == self.request.user

class TributeCreateView(LoginRequiredMixin, CreateView):
    model = Tribute
    template_name = 'tribute_new.html'
    fields = FIELDS
    login_url = 'login'
    
    def form_valid(self, form):
        ''' Set the user which send the request as the form 'creator' '''
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Set the user wich send the request as the form 'creator' '''
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('tribute_detail', args=[str(self.id)])

