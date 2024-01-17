from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import DatosAgrarios
from .forms import DatosAgrariosFilterForm
from django.core.paginator import Paginator


# Create your views here.
# en tu_app/views.py


def mostrarDatos(request):
    form = DatosAgrariosFilterForm(request.GET)
    queryset = DatosAgrarios.objects.all()  # Obtén las primeras 10 filas
    anyo_filtro = request.GET.get('anyo')
    semana_filtro = request.GET.get('semana')
    # variedad_filtro = request.GET.get('anyo')

    if form.is_valid():
        if anyo_filtro != "0" and anyo_filtro is not None:
            queryset = queryset.filter(anyo_precio=anyo_filtro)
        # Agrega lógica similar para otros campos del formulario según sea necesario
        if semana_filtro != "0" and semana_filtro is not None:
            queryset = queryset.filter(semana_precio=semana_filtro)
        # if variedad_filtro != "0" and variedad_filtro is not None:
        #     queryset = queryset.filter(anyo_precio=variedad_filtro)

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)
    
    return render(request, 'datosagrarios/datos.html', {'form': form, 'data': queryset})
