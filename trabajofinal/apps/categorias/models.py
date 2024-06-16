from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    img = models.ImageField(null=True, blank=True, upload_to='archivo/cat')
    def __str__(self):
        return self.nombre

# Create your models here.
