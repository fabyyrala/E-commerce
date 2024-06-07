from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "Productos"

urlpatterns = [
    path('catalogo/', views.Catalogo, name="Catalogo"),
    path('detalles/<int:pk>', views.DetalleProducto.as_view(), name="Detalles"),

]
