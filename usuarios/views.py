from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def inicio(request):
    return render(request, 'inicio.html')

def alumnos_view(request):
    return render(request, 'alumnos.html')

def agregar_view(request):
    return render(request, 'agregar.html')

def subir_view(request):
    return render(request, 'subir.html')

def parcial(request):
    return render(request, 'parcial.html')

def niveles(request):
    return render(request, 'niveles.html')

def base(request):
    return render(request, 'base.html')