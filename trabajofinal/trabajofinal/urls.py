from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Incio, name="inicio"),
    path('error-permisos/', views.pagina_error_permisos, name="error_permisos"),

    #Incluye aplicacion
    #usuarios
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include("apps.usuarios.urls")),
    
   

    
    
    #productos
    path('', include("apps.productos.urls")),
]
