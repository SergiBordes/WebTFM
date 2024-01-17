import csv
from datosagrarios.models import DatosAgrarios
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Importar datos desde un archivo CSV'

    def handle(self, *args, **options):
        csv_file_path = 'datosagrarios/datoscsv/precios_agrarios_comunitat_valenciana.csv'  # Reemplaza con la ruta real de tu archivo CSV

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                DatosAgrarios.objects.create(
                    anyo_precio=row['Anyo Precio'],
                    semana_precio=row['Semana Precio'],
                    codigo_grupo_producto=row['Código Grupo Producto'],
                    grupo_producto_castellano=row['Grupo Producto castellano'],
                    grupo_producto_valenciano=row['Grupo Producto valenciano'],
                    codigo_producto=row['Código Producto'],
                    producto_castellano=row['Producto castellano'],
                    producto_valenciano=row['Producto valenciano'],
                    codigo_variedad=row['Código Variedad'],
                    variedad_castellano=row['Variedad castellano'],
                    variedad_valenciano=row['Variedad valenciano'],
                    codigo_zona=row['Código Zona'],
                    zona_castellano=row['Zona castellano'],
                    zona_valenciano=row['Zona valenciano'],
                    precio_minimo=row['Precio Mínimo'].replace(',', '.'),
                    precio_medio=row['Precio Medio'].replace(',', '.'),
                    precio_maximo=row['Precio Máximo'].replace(',', '.'),
                )
