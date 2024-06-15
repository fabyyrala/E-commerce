from django.shortcuts import get_object_or_404, redirect,render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from apps.productos.models import Producto
from apps.productos.formularios import NuevoProducto
from apps.categorias.models import Categoria
from apps.favorito.models import Favorito

class Catalogo(ListView):
    template_name= 'productos/catalogo.html'
    model = Producto
    context_object_name = "productos"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        ctx = super(Catalogo, self).get_context_data(**kwargs)
        return ctx
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()

        #favoritos
        usuario = self.request.user
        
        productos_favoritos = Favorito.objects.filter(usuario=usuario).values_list('producto__id', flat=True)
        for producto in context['productos']:
            producto.es_favorito = producto.id in productos_favoritos

        
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria__nombre=categoria)
        return queryset

  

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




    
    