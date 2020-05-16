from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Memorial 
from .forms import MemorialForm
# Create your views here.

#required, field atribute
FIELDS = ('first_name', 'second_first_name', 'last_name', 'second_last_name',
          'biography' , 'date_of_birth', 'date_of_passing', 'profile_image' ,
          'cover_image' )



class MemorialListView(ListView):
    model = Memorial
    template_name = 'memorial_list.html'

class MemorialDetailView(DetailView):
    model = Memorial
    template_name = 'memorial_detail.html'

class MemorialCreateView(LoginRequiredMixin, CreateView):
    template_name = 'memorial_new.html'
    form_class = MemorialForm
    login_url = 'login'
    success_url = reverse_lazy('memorial_list')
    # Set the default logged in user as the autho of the memorial
    def form_valid(self, form):
        form.instance.autho = self.request.user
        return  super().form_valid(form)

class MemorialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Memorial
    template_name = 'memorial_update.html'
    login_url = 'login'
    success_url = reverse_lazy('memorial_list')
    fields = FIELDS    
    # test that the logged in user matches the one whos the memorial belong to 
    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user 

class MemorialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Memorial
    template_name = 'memorial_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('memorial_list')
    fields = FIELDS    

    # test that the logged in user matches the one whos the memorial belong to 
    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user 
