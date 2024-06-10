from django.contrib import admin
from django.urls import path, include
from . import views
from . views import VerPerfil

app_name = "Usuarios"

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('registro', views.registrarusuario, name="registrarusuario"),
    path('listar-usuarios',views.ListarUsuarios.as_view(), name="listar-usuarios"),
    path('perfil', views.VerPerfil.as_view(), name="perfil"),
    path('perfil/<int:usuario_id>/', VerPerfil.as_view(), name='ver_perfil'),
    path('perfil/editar/<int:pk>', views.EditarPerfil.as_view(), name="EditarPerfil")
    
    
    
    #path('', views.Incio, name="inicio"),
]

