# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import folium

# Create your views here.
def map(request):
    
    mapa = folium.Map(location=[39.4630349,-0.3774392], zoom_start = 11, min_zoom=9)
    
    # Agregar marcadores para Valencia, Alicante y Castellón
    valencia_coords = [39.4699, -0.3763]
    alicante_coords = [38.3452, -0.4810]
    castellon_coords = [39.9864, -0.0513]

    folium.Marker(location=valencia_coords, popup='Valencia').add_to(mapa)
    folium.Marker(location=alicante_coords, popup='Alicante').add_to(mapa)
    folium.Marker(location=castellon_coords, popup='Castellón').add_to(mapa)


    context = {'map': mapa._repr_html_()}
    return render(request, 'map/mapa.html', context)