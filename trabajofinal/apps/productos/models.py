from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre  = models.CharField(max_length=130)
    desc  = models.CharField(max_length=240)
    categoria =models.ForeignKey(Categoria, on_delete=models.CASCADE, default=True, null = False)
    precio = models.FloatField()
    activo  = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
    

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    
