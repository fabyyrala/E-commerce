"""
URL configuration for trabajofinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

