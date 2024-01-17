# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import folium

# Create your views here.
def map(request):
    
    initialMap = folium.Map(location=[39.4630349,-0.3774392], zoom_start = 9)
    
    context = {'map': initialMap._repr_html_()}
    return render(request, 'map/mapa.html', context)