from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre  = models.CharField(max_length=130)
    desc  = models.CharField(max_length=240)
    categoria = models.CharField(max_length=30)
    precio = models.FloatField()
    activo  = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"