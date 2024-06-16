from django.shortcuts import render
from apps.categorias.models import Categoria
from apps.productos.models import Producto
from django.views.generic.edit import CreateView

def Incio(request):
    ctx = { 
        "categorias": Categoria.objects.all(),
        "productos": Producto.objects.all().latest()
    }

    return render(request, 'inicio.html', ctx)

def pagina_error_permisos(request):
    template_name = 'paginas/error_permisos.html'

    ctx = {

    }
    return render(request, template_name, ctx)