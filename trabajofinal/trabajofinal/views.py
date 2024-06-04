from django.shortcuts import render

def Incio(request):
    return render(request, 'inicio.html', {})

