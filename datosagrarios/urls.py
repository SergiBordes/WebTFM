from django.urls import path
from . import views

urlpatterns = [
    path('datosagrarios/', views.mostrarDatos, name='datosagrarios-datos'),
]
