from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import DatosAgrarios
from .forms import DatosAgrariosFilterForm
from django.core.paginator import Paginator
from .datoscsv.datamain import obtenerVariedades

# Create your views here.
# en tu_app/views.py


def mostrarDatos(request):
    semanas = list(range(1, 48))
    productos = obtenerVariedades
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
    
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)
    
    # Agrega los parámetros de filtro a la URL de paginación
    queryset.paginator.baseurl = f"?page={page_number}" + f"&anyo={request.GET.get('anyo')}" + f"&semana={request.GET.get('semana')}" + f"&producto={request.GET.get('producto')}"
    
    return render(request, 'datosagrarios/datos.html', {'form': form, 'data': queryset, 'semanas': semanas, 'productos': productos, 'total_filas': total_filas})


