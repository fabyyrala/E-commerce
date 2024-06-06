from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre  = models.CharField()
    desc  = models.CharField()
    categoria = models.CharField()
    precio = models.FloatField()
    estado  = models.BooleanField()