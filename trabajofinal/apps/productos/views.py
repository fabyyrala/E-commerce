from django.shortcuts import render

def Catalogo(request):
    return render(request, 'catalogo.html', {})
