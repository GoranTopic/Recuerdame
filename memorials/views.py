from django.shortcuts import render
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
def ImageFormView(request, memorial_pk):
    #ArticleFormSet = formset_factory(ArticleForm)
    form = ImageForm(request.POST)
    context = {} 

    print(request.POST)
    if request.method == 'POST':
        print("GOT POST")
        # if the user send Post request
        #formset = ArticleFormSet(request.POST, request.FILES)
        if form.is_valid():
            print("GOT VALID FORM")
            # if the form is valid trought the TributeForm 
            # set request user as tribute user
            form.instance.user = request.user
            # set the intance of memorial
            form.instance.memorial = Memorial.objects.get(pk=memorial_pk)
            # the files from the post request 
            files = request.FILES 
            # the image of the cover
            print(request.instance)
            form.instance.picture = files['picture']
            # create instance of tribute model
            form.save()
        context['form'] = form
        return HttpResponseRedirect(reverse('memorial_detail', kwargs={'pk': memorial_pk}))
    else:
        #other request method such as GET
        form = ImageForm()
        context['form'] = form
        return render(request, 'image_new.html', context)
