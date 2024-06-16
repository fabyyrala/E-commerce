from django.db import models
from apps.categorias.models import Categoria


class Producto(models.Model):
    nombre = models.CharField(max_length=130)
    desc = models.CharField(max_length=240)
    precio = models.FloatField()
    activo = models.BooleanField(default=True)
    img = models.ImageField(default=None, blank=True, upload_to='archivo/productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) 
    fechacreacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.categoria.nombre}"


    





