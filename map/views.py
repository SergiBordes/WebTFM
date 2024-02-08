# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import folium
import pandas
import requests
import json
from django.contrib.auth.decorators import login_required
from datosagrarios.forms import DatosAgrariosFilterForm
from datosagrarios.models import DatosAgrarios
from datosagrarios.datoscsv.datamain import obtenerVariedades, precio_medio_variedad_por_provincia



geo_json_data = requests.get(
    "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/spain-provinces.geojson"
).json()

precios_medios = []


# Create your views here.
@login_required()
def map(request):
    form = DatosAgrariosFilterForm(request.GET)
    queryset = DatosAgrarios.objects.all()

    variedades = obtenerVariedades()
    
    if request.method == 'GET':
        anyo_filtro = request.GET.get('anyo')
        variedad_filtro = request.GET.get('variedad')
        if anyo_filtro is not None and variedad_filtro is not None:
            precios_medios  = precio_medio_variedad_por_provincia(str(variedad_filtro), int(anyo_filtro))
            print("################## -->" + str(precios_medios))
        else:
            precios_medios = None  # O cualquier otro valor predeterminado que desees
    
    m = folium.Map([39.4630349,-0.3774392], tiles="cartodbpositron", zoom_start = 8, min_zoom=7)

    folium.GeoJson(
        geo_json_data,
        style_function=lambda feature: {
            "fillColor": my_color_function(feature, precios_medios),
            "color": "black",
            "weight": 2,
            "dashArray": "5, 5",
            "tooltip": "prueba??",
        },
    ).add_to(m)
    
    context = {'map': m._repr_html_(), 'variedades': variedades}
    return render(request, 'map/mapa.html', context)


def my_color_function(feature, precios_medios):
    """Asigna colores a las provincias según su nombre."""
    name = feature["properties"]["name"]
    if precios_medios is None or precios_medios == []:
        if name == "València/Valencia" or name == "Alacant/Alicante" or name == "Castelló/Castellón":
            return "#0000ff"  # Rojo para Valencia
        else:
            return "#808080"  # Color gris para otras provincias
    else:
        if len(precios_medios) > 0  and name == precios_medios[0]["provincia"]:
            return "#CB3234"
        if len(precios_medios) > 1  and name == precios_medios[1]["provincia"]:
            return "#FF8000"
        if len(precios_medios) > 2  and name == precios_medios[2]["provincia"]:
            return "#008F39"
    