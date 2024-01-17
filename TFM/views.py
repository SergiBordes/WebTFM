from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

#Local imports
from . import models

TFMs = [{
    'author':'Dom', 
    'title':'Prueba de titulo', 
    'directions':'direcciones', 
    'fecha_post':'05 de Enero 2024', 
}, 
{
    'author':'Dom', 
    'title':'Segunda Prueba', 
    'directions':'direcciones', 
    'fecha_post':'05 de Febrero 2024', 
}]

# Create your views here.
def home(request):
    recetas = models.Receta.objects.all()
    context = {
        'recetas' : recetas
    }
    return render(request, "TFM/home.html", context)

class RecetaListView(ListView):
    model = models.Receta
    template_name = 'TFM/home.html'
    context_object_name = 'recetas'
    
class RecetaDetailView(DetailView):
    model = models.Receta
    template_name = 'TFM/TFM_detail.html' #Si nuestra página no se llama receta_detail (como el nombre de la clase), tendremos que pasarle la referencia de la página en esta variable
    
class RecetaCreateView(LoginRequiredMixin, CreateView):
    model = models.Receta
    template_name = 'TFM/TFM_form.html'
    fields = ['titulo', 'descripcion']
    
    def form_valid(self, form): #Aqui le decimos que ponga como author al usuario que esta añadiendo la receta
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecetaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Receta
    template_name = 'TFM/TFM_form.html'
    fields = ['titulo', 'descripcion']
    
    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.author
    
    def form_valid(self, form): #Aqui le decimos que ponga como author al usuario que esta añadiendo la receta
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecetaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Receta
    template_name = 'TFM/TFM_confirm_delete.html'
    success_url = reverse_lazy('TFM-home')
    
    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.author

def about(request):
    return render(request, "TFM/about.html")

def index(request):
    return render(request, "TFM/index.html")