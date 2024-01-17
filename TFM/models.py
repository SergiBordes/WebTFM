from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("TFM-detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.titulo