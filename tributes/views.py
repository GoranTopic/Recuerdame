from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Tribute
from memorials.models import Memorial
from .forms import TributeForm
from django.urls import reverse, reverse_lazy 
from django.http import HttpResponseRedirect
# Create your views here.

# requiered field attibutes
FIELDS = ('quote', 'anecdote', 'writting', 'cover_image')

def create_view(request, memorial_pk):
    context = {} 

    if request.method == 'POST':
        form = TributeForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.instance.memorial = Memorial.objects.get(pk=memorial_pk)
            form.save()

        context['form'] = form
        return HttpResponseRedirect(reverse('memorial_detail', kwargs={'pk': memorial_pk}))


    else:
        form = TributeForm()
        context['form'] = form
        return render(request, 'tribute_new.html', context)


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
    
    def get_object(self, **kwargs ):
        print("------- I RAN ---------")
        print(kwargs)
        return models.todo.objects.get(id=self.kwargs['post'])

    def form_valid(self, form):
        ''' Set the user which send the request as the form 'creator' '''
        form.instance.user = self.request.user
        print(self.post)
        form.instance.memorial = self.post
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Set the user wich send the request as the form 'creator' '''
        form.instance.user = self.request.user
        print(self.post)
        form.instance.memorial = self.post
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('tribute_detail', args=[str(self.id)])

