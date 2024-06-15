from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse_lazy

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias/lista_categorias.html'
    context_object_name = 'categorias'
    paginate_by = 4
    def get_context_data(self, **kwargs):
        ctx = super(CategoriaListView, self).get_context_data(**kwargs)
        return ctx
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/crear_categoria.html'
    success_url = reverse_lazy('Categorias:lista_categorias')

    def form_valid(self, form):
        # Aquí es donde puedes procesar el formulario y guardar la categoría en la base de datos
        # Puedes acceder a los datos del formulario a través de form.cleaned_data
        # Por ejemplo, para guardar la categoría:
        categoria = form.save(commit=False)  # Guarda pero no confirma
        # Realiza cualquier manipulación adicional de la categoría aquí si es necesario
        categoria.save()  # Ahora sí guarda definitivamente

        return super().form_valid(form)

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/editar_categoria.html'
    success_url = reverse_lazy('Categorias:lista_categorias')

    def get_object(self, queryset=None):
        categoria_id = self.kwargs['pk']
        return self.model.objects.get(id=categoria_id)

    def form_valid(self, form):
        categoria = form.save()
        return super().form_valid(form)

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categorias/eliminar_categoria.html'
    success_url = reverse_lazy('lista_categorias')

# Create your views here.
