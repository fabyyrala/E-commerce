from django.shortcuts import get_object_or_404, redirect,render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Favorito,Categoria

from apps.productos.models import Producto,Categoria
from apps.productos.formularios import NuevoProducto

class Catalogo(ListView):
    template_name= 'productos/catalogo.html'
    model = Producto
    context_object_name = "productos"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        ctx = super(Catalogo, self).get_context_data(**kwargs)
        return ctx
    
    #def get_queryset(self):
        #return self.model.objects.all().order_by('-id')

    #Catalogo por categoria Modificar si no funciona
    def get_queryset(self):
        return self.model.objects.all().order_by('categoria')


class DetalleProducto(DetailView):
    templates_name = 'productos/producto_detail.html'
    model = Producto

    def get_context_data(self, **kwargs):
        ctx = super(DetalleProducto, self).get_context_data(**kwargs)
        ctx["icono"] = "o"
        return ctx
    
    def get_queryset(self):
        return self.model.objects.all().order_by('id')


class RegistrarProducto(CreateView):
    template_name = "productos/nuevo.html"
    model = Producto
    form_class = NuevoProducto
    success_url = reverse_lazy("Productos:Catalogo")


class EditarProducto(UpdateView):
    template_name = "productos/editar.html"
    model = Producto
    form_class = NuevoProducto
    success_url = reverse_lazy("Productos:Catalogo")


def agregar_favorito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    Favorito.objects.create(usuario=request.user, producto=producto)
    return redirect('Productos:Catalogo')



    
    