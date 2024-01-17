from django.db import models

# Create your models here.

# en tu_app/models.py
from django.db import models

class DatosAgrarios(models.Model):
    anyo_precio = models.IntegerField()
    semana_precio = models.IntegerField()
    codigo_grupo_producto = models.IntegerField()
    grupo_producto_castellano = models.CharField(max_length=255)
    grupo_producto_valenciano = models.CharField(max_length=255)
    codigo_producto = models.IntegerField()
    producto_castellano = models.CharField(max_length=255)
    producto_valenciano = models.CharField(max_length=255)
    codigo_variedad = models.IntegerField()
    variedad_castellano = models.CharField(max_length=255)
    variedad_valenciano = models.CharField(max_length=255)
    codigo_zona = models.IntegerField()
    zona_castellano = models.CharField(max_length=255)
    zona_valenciano = models.CharField(max_length=255)
    precio_minimo = models.FloatField()
    precio_medio = models.FloatField()
    precio_maximo = models.FloatField()

    def __str__(self):
        return f"{self.anyo_precio} - {self.semana_precio} - {self.producto_castellano} - {self.zona_castellano}"
