from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "Categorias"
urlpatterns = [
    # Ruta para la lista de categorías
    path('lista-categorias/', views.CategoriaListView.as_view(), name='lista_categorias'),
    
    
    # Ruta para crear una nueva categoría
    path('crear-categoria/', views.CategoriaCreateView.as_view(), name='crear_categoria'),
    
    # Ruta para editar una categoría existente
    path('editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
    
    # Ruta para eliminar una categoría
    path('eliminar/<int:pk>/', views.CategoriaDeleteView.as_view(), name='eliminar_categoria'),
]