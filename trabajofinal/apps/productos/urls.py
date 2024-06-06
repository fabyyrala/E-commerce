from django.contrib import admin
from django.urls import path, include
from . import views

name_app = "Productos"

urlpatterns = [
    path('catalogo/', views.Catalogo, name="Catalogo"),

]
