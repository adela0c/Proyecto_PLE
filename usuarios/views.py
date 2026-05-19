from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def alumnos_view(request):
    return render(request, 'alumnos.html')

def agregar_view(request):
    return render(request, 'agregar.html')

def subir_view(request):
    return render(request, 'subir.html')