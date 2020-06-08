from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Tribute
from .forms import TributeForm
from memorials.models import Memorial
from django.urls import reverse, reverse_lazy 
from django.http import HttpResponseRedirect
# Create your views here.

# requiered field attibutes
FIELDS = ('quote', 'quote_author', 'anecdote', 'writting', 'cover_image')



def create_view(request, memorial_pk):
    context = {} 
    if request.method == 'POST':
        # if the user sendPost request
        form = TributeForm(request.POST)
        if form.is_valid():
            # if the form is valid trought the TributeForm 
            # set request user as tribute user
            form.instance.user = request.user
            # set the intance of memorial
            form.instance.memorial = Memorial.objects.get(pk=memorial_pk)
            # the files from the post request 
            files = request.FILES 
            # the image of the cover
            form.instance.cover_image = files['cover_image']
            # create instance of tribute model
            form.save()
        context['form'] = form
        return HttpResponseRedirect(reverse('memorial_detail', kwargs={'pk': memorial_pk}))
    else:
        #other request method such as GET
        form = TributeForm()
        context['form'] = form
        return render(request, 'tribute_new.html', context)


class TributeDetailView(DetailView):
    model = Tribute
    template_name = 'tribute_detail.html'

class TributeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tribute
    template_name = 'tribute_update.html'
    fields = FIELDS
    login_url = 'login'
    #success_url = reverse_lazy('tribute_detail')
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
    login_url = 'login'
    #success_url = reverse_lazy('tribute_detail')
    def test_func(self):
        ''' checks if the user is the same as the creator '''
        obj = self.get_object()
        return obj.user == self.request.user

