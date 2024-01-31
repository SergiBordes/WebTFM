# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import folium
import pandas
import requests
import json
from datosagrarios.forms import DatosAgrariosFilterForm
from datosagrarios.models import DatosAgrarios
from datosagrarios.datoscsv.datamain import obtenerVariedades, precio_medio_variedad_por_provincia



geo_json_data = requests.get(
    "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/spain-provinces.geojson"
).json()


# Create your views here.
def map(request):
    form = DatosAgrariosFilterForm(request.GET)
    queryset = DatosAgrarios.objects.all()

    variedades = obtenerVariedades()
    
    mapa = folium.Map(location=[39.4630349,-0.3774392], tiles="cartodbpositron", zoom_start = 11, min_zoom=9)

    m = folium.Map([39.4630349,-0.3774392], tiles="cartodbpositron", zoom_start = 8, min_zoom=7)

    folium.GeoJson(
        geo_json_data,
        style_function=lambda feature: {
            "fillColor": my_color_function(feature),
            "color": "black",
            "weight": 2,
            "dashArray": "5, 5",
        },
    ).add_to(m)
    
    if request.method == 'GET':
        anyo_filtro = request.GET.get('anyo')
        variedad_filtro = request.GET.get('variedad')
        print("==================== pruebas--> Año: " + str(anyo_filtro) + " ;   Variedad: " + str(variedad_filtro))
        precios_medios  = precio_medio_variedad_por_provincia(str(variedad_filtro), str(anyo_filtro))
        print("################## -->" + json.dumps(precios_medios))
    
    context = {'map': m._repr_html_(), 'variedades': variedades}
    return render(request, 'map/mapa.html', context)


def my_color_function(feature):
    """Asigna colores a las provincias según su nombre."""
    name = feature["properties"]["name"]
    if name == "València/Valencia":
        return "#ff0000"  # Rojo para Valencia
    elif name == "Alacant/Alicante":
        return "#00ff00"  # Verde para Alicante
    elif name == "Castelló/Castellón":
        return "#0000ff"  # Azul para Castellón
    else:
        return "#808080"  # Color gris para otras provincias
