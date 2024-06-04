from apps.usuarios.formularios import FormularioRegistroUsuario

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
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