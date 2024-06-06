from django.shortcuts import render
from apps.productos.models import Producto

def Catalogo(request):
    ctx = {
        "Producto": Producto.objects.all()
    }
    return render(request, 'productos/catalogo.html', ctx)
