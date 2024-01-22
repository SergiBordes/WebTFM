from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import DatosAgrarios
from .forms import DatosAgrariosFilterForm
from django.core.paginator import Paginator
from .datoscsv.datamain import obtenerProductos, obtenerVariedades, media_precio_por_anyo

from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
import base64

# Create your views here.
# en tu_app/views.py
plt.switch_backend('Agg')

@csrf_exempt
def mostrarDatos(request):
    semanas = list(range(1, 48))
    productos = obtenerProductos()
    variedades = obtenerVariedades()
    form = DatosAgrariosFilterForm(request.GET)
    queryset = DatosAgrarios.objects.all()
    anyo_filtro = request.GET.get('anyo')
    semana_filtro = request.GET.get('semana')
    producto_filtro = request.GET.get('producto')
    # variedad_filtro = request.GET.get('anyo')

    if form.is_valid():
        #Filtramos anyo
        if anyo_filtro != "0" and anyo_filtro is not None:
            print("se filtra por año")
            queryset = queryset.filter(anyo_precio=anyo_filtro)
            
        # Filtramos semana
        if semana_filtro != "0" and semana_filtro is not None:
            print("se filtra por semana")
            queryset = queryset.filter(semana_precio=semana_filtro)
        
        #Filtramos variedad 
        if producto_filtro != "0" and producto_filtro is not None:
            print("se filtra por producto")
            queryset = queryset.filter(producto_castellano=producto_filtro)

    total_filas = queryset.count()
    
    paginator = Paginator(queryset, 20)
    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)
    
    # Agrega los parámetros de filtro a la URL de paginación
    queryset.paginator.baseurl = f"?page={page_number}" + f"&anyo={request.GET.get('anyo')}" + f"&semana={request.GET.get('semana')}" + f"&producto={request.GET.get('producto')}"# Datos de ejemplo (puedes reemplazarlos con tus propios datos)

    datagrafica = []
    
    deslizar = "topPagina"
    
    if request.method == 'POST':
        # Verificar si el botón del Formulario 2 se ha presionado
        if 'btnGrafica' in request.POST:
            # Realizar acciones específicas para el Formulario 2
            variedadGrafica = request.POST['variedadGrafica']
            print('Valor del campo del Formulario 2:', variedadGrafica)
            datagrafica = media_precio_por_anyo(variedadGrafica)
            deslizar = "chartContainer"

    # Agrega 'variedades' al contexto
    context = {
        'form': form,
        'data': queryset,
        'semanas': semanas,
        'productos': productos,
        'total_filas': total_filas,
        'stepcount': datagrafica,
        'variedades': variedades,
        'deslizar': deslizar,
    }
    return render(request, 'datosagrarios/datos.html', context)


