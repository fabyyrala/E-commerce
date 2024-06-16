from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Incio, name="inicio"),
    path('error-permisos/', views.pagina_error_permisos, name="error_permisos"),

    #Incluye aplicacion
    #usuarios
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include("apps.usuarios.urls")),
    
    
    #productos
    path('prod/', include("apps.productos.urls")),
    
    #categorias
    path('categorias/', include('apps.categorias.urls')),
    path('favs/', include('apps.favorito.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
