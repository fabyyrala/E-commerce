from django.db import models
from django.contrib.auth.models import User

from apps.productos.models import Producto


# Create your models here.

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.producto}"