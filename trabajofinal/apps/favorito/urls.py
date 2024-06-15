from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "Favorito"

urlpatterns = [
    path('listarfavoritos/<int:user_id>', views.ListarFavorito, name="ListarFavoritos"), 
    path('crear-fav/prod/<int:producto_id>', views.CrearFavorito, name="CrearFavorito"), 
    path('eliminar-fav/prod/<int:producto_id>', views.EliminarFavorito, name="EliminarFavorito"), 
    
]

