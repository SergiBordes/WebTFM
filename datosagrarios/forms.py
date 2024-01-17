# en datosagrarios/forms.py
from django import forms

class DatosAgrariosFilterForm(forms.Form):
    # Define los campos del formulario para el filtrado
    anyo_precio = forms.IntegerField(label='Año Precio', required=False)
    precio = forms.IntegerField(label='Precio', required=False)
    # Agrega otros campos según tus necesidades
