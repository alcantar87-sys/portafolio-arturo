from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def fn_response(request):
    #return HttpResponse("Hola Mundo. Esto es una prueba.")
    context = {'greeting': 'Hello, World!'}
    # Combines request, template path, and data
    return render(request, 'core/home.html', context)


def fn_about(request):
    context = {'title':'About'}
    # Combines request, template path, and data
    return render(request, 'core/about.html', context)


def fn_projects(request):
    context = {'title':'Projects'}
    # Combines request, template path, and data
    return render(request, 'core/projects.html', context)