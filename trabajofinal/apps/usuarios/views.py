from typing import Any

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from apps.usuarios.formularios import FormularioRegistroUsuario

# Create your views here.
def login_user(request):
   if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.success(request, "Usuario y/o contraseña incorrecto.")
            return redirect('Usuarios:login')
   else:
        return render(request, 'aut/login.html', {})
   

def logout_user(request):
    logout(request)
    return redirect('inicio')


def registrarusuario(request):
    form = FormularioRegistroUsuario()

    if request.method == "POST":
        form = FormularioRegistroUsuario(request.POST) 
        if form.is_valid():
            form.save()
            # Tiene que corresponder a cada espacio de la BD de manera manual.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password= password)
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect('inicio')
        else:
            pass

    ctx = {
        "formulario": form,
    }
        
    return render(request, 'registrarse.html', ctx)

class ListarUsuarios(LoginRequiredMixin,ListView):
    template_name = 'usuarios/listar_usuarios.html'
    model = User
    context_object_name = 'usuarios'
    paginate = 10
    
    def get_context_data(self,**kwargs):
        ctx = super(ListarUsuarios,self).get_context_data(**kwargs)
        return ctx
    
    def get_queryset(self):
        return self.model.objects.all() 



class VerPerfil(DetailView):
    model = User
    template_name = 'usuarios/perfil.html'
    context_object_name = 'usuario'
    def get_object(self):
        return self.get_queryset().first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.object
        return context
    
    
@login_required
def perfil(request):
    # Aquí puedes mostrar el perfil del usuario loggeado
    
    return render(request, 'perfil.html')



class EditarPerfil(UpdateView):
    template_name = "usuarios/editarperfil.html"
    model = User
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy("Usuarios:EditarPerfil")
