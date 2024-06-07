
from apps.productos.models import Producto

from django.shortcuts import render
from django.views.generic.detail import DetailView



def Catalogo(request):
    ctx = {
        "Producto": Producto.objects.all()
    }
    return render(request, 'productos/catalogo.html', ctx)


class DetalleProducto(DetailView):
    templates_name = 'productos/producto_detail.html'
    model = Producto

    def get_context_data(self, **kwargs):
        ctx = super(DetalleProducto, self).get_context_data(**kwargs)
        ctx["icono"] = "o"
        return ctx
    
    def get_queryset(self):
        return self.model.objects.all().order_by('id')

