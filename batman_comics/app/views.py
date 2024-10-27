from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'app/inicio.html')


def historia(request):
    return render(request, 'app/historia.html')


def enemigos(request):
    return render(request, 'app/enemigos.html')


def curiosidades(request):
    return render(request, 'app/curiosidades.html')


def aliados(request):
    return render(request, 'app/aliados.html')

