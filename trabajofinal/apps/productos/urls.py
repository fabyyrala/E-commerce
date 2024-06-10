from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "Productos"

urlpatterns = [
    path('catalogo/', views.Catalogo.as_view(), name="Catalogo"),
    path('nuevo/', views.RegistrarProducto.as_view(), name="NuevoProducto"),
    path('editar/<int:pk>', views.EditarProducto.as_view(), name="EditarProducto"),
    path('detalles/<int:pk>', views.DetalleProducto.as_view(), name="Detalles"),
    path('categorias/<str:foo>', views.Categoria, name="Categoria"),

]
