import django_filters
from .models import DatosAgrarios

class DatosAgrariosFilter(django_filters.FilterSet):
    
    class Meta:
        model = DatosAgrarios
        fields = [
            'anyo_precio',
            'semana_precio',
            'producto_castellano',
        ]