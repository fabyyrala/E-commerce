from django.shortcuts import render

def Incio(request):
    return render(request, 'inicio.html', {})

def pagina_error_permisos(request):
    template_name = 'paginas/error_permisos.html'

    ctx = {

    }
    return render(request, template_name, ctx)