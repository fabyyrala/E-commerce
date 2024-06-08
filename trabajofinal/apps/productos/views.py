from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView


from apps.productos.models import Producto
from apps.productos.formularios import NuevoProducto

class Catalogo(ListView):
    template_name= 'productos/catalogo.html'
    model = Producto
    context_object_name = "productos"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        ctx = super(Catalogo, self).get_context_data(**kwargs)
        return ctx
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


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
