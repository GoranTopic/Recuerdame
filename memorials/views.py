from django.shortcuts import render
from django.forms import formset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Memorial
from .forms import ImageForm
# Create your views here.

# requiered field attibutes
FIELDS = ( 'nombre', 'segundo_nombre', 'apellido', 'segundo_apellido',
           'biografia' , 'fecha_de_nacimiento', 'fecha_de_muerte',  
           'imagen_de_perfil', 'imagen_de_fondo', 'pais', 'epitafo', )

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
        return obj.creado_por == self.request.user

class MemorialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Memorial
    template_name = 'memorial_delete.html'
    fields = FIELDS
    success_url = reverse_lazy('memorial_list')
    def test_func(self):
        ''' checks if the user is the same as the creator '''
        obj = self.get_object()
        return obj.creado_por == self.request.user

class MemorialCreateView(LoginRequiredMixin, CreateView):
    model = Memorial
    template_name = 'memorial_new.html'
    fields = FIELDS
    login_url = 'login'
    
    def form_valid(self, form):
        ''' Set the user wich send the request as the form 'creator' '''
        form.instance.creado_por = self.request.user
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' Set the user wich send the request as the form 'creator' '''
        form.instance.creado_por = self.request.user
        form.instance.manager = self.request.user
        return super().form_valid(form)


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def lifeEvenFormView(request, memorial_pk):
    memorial = Memorial.objects.get(pk=memorial_pk)
    context = {} 
    LifeEventFormSet = formset_factory(
            LifeEvenForm, 
            extra=10,
            max_num=11,
            min_num=1)

    if request.method == 'POST':
        formset = LifeFormSet(request.POST, request.FILES)
        # if the user send Post request
        #formset = ArticleFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # if the form is valid trought the TributeForm 
            # set request user as tribute user
            formset.instance.user = request.user
            # set the intance of memorial
            form.instance.memorial = memorial
            # the files from the post request 
            files = request.FILES 
            # the image of the cover
            form.instance.picture = files['picture']
            # create instance of tribute model
            form.save()
        context['formset'] = formset
        return HttpResponseRedirect(reverse('memorial_detail', kwargs={'pk': memorial_pk}))
    else:
        #other request method such as GET
        formset = LifeEventFormSet()
        context['formset'] = formset
        return render(request, 'image_new.html', context)
