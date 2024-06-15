from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from apps.productos.models import Producto
from .models import Favorito

def ListarFavorito(request, user_id):
    ctx = { 
        "favoritos": Favorito.objects.filter(usuario__id=user_id),
    }

    return render(request, 'productos/listarfavoritos.html', ctx)


@login_required
def CrearFavorito(request, producto_id):
    producto = get_object_or_404(Producto, id= producto_id)
    Favorito.objects.get_or_create(usuario=request.user, producto=producto)
    
    return redirect("Productos:Catalogo")


def EliminarFavorito(request, producto_id):
    producto = get_object_or_404(Producto, id= producto_id)
    favorito = get_object_or_404(Favorito, usuario=request.user, producto=producto)

    favorito.delete()
    
    return redirect("Productos:Catalogo")

