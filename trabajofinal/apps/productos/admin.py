from django.contrib import admin
from .models import Producto, Favorito,Categoria

# Register your models here.
admin.site.register(Producto)
admin.site.register(Favorito)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

admin.site.register(Categoria, CategoriaAdmin)