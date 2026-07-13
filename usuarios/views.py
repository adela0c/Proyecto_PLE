import pandas as pd

from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Alumno, Categoria


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Alumno, Categoria


# ==========================
# LOGIN
# ==========================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("inicio")

        else:

            messages.error(
                request,
                "Usuario o contraseña incorrectos."
            )

    return render(request, "login.html")


# ==========================
# INICIO
# ==========================

def inicio_view(request):

    return render(request, "inicio.html")


# ==========================
# LISTA DE ALUMNOS
# ==========================

def alumnos_view(request):

    alumnos = Alumno.objects.select_related(
        "categoria"
    ).all()

    return render(
        request,
        "alumnos.html",
        {
            "alumnos": alumnos
        }
    )


# ==========================
# REGISTRAR ALUMNO
# ==========================

def agregar_view(request):

    categorias = Categoria.objects.all()

    if request.method == "POST":

        categoria = Categoria.objects.get(
            id=request.POST["categoria"]
        )

        Alumno.objects.create(

            nombre=request.POST["nombre"],
            apellido_paterno=request.POST["apellido_paterno"],
            apellido_materno=request.POST["apellido_materno"],
            telefono=request.POST["telefono"],
            correo=request.POST["correo"],
            fecha_nacimiento=request.POST["fecha_nacimiento"],

            tutor_nombre=request.POST.get("tutor_nombre"),
            tutor_telefono=request.POST.get("tutor_telefono"),

            categoria=categoria,

            status=request.POST.get("status") == "True",

            foto=request.FILES.get("foto")

        )

        return redirect("alumnos")

    return render(
        request,
        "agregar.html",
        {
            "categorias": categorias
        }
    )


# ==========================
# SUBIR ARCHIVOS
# ==========================

def subir_view(request):

    return render(
        request,
        "subir.html"
    )


# ==========================
# NIVELES
# ==========================

def niveles_view(request):

    return render(
        request,
        "niveles.html"
    )


# ==========================
# PARCIALES
# ==========================

def parcial_view(request):

    return render(
        request,
        "parcial.html"
    )


# ==========================
# EDITAR ALUMNO
# ==========================

def editar_alumno(request, id):

    alumno = get_object_or_404(
        Alumno,
        id=id
    )

    categorias = Categoria.objects.all()

    if request.method == "POST":

        alumno.nombre = request.POST["nombre"]
        alumno.apellido_paterno = request.POST["apellido_paterno"]
        alumno.apellido_materno = request.POST["apellido_materno"]
        alumno.telefono = request.POST["telefono"]
        alumno.correo = request.POST["correo"]
        alumno.fecha_nacimiento = request.POST["fecha_nacimiento"]
        alumno.tutor_nombre = request.POST.get("tutor_nombre")
        alumno.tutor_telefono = request.POST.get("tutor_telefono")
        alumno.status = request.POST.get("status") == "True"

        alumno.categoria = Categoria.objects.get(
            id=request.POST["categoria"]
        )

        if request.FILES.get("foto"):

            alumno.foto = request.FILES["foto"]

        alumno.save()

        return redirect("alumnos")

    return render(
        request,
        "agregar.html",
        {
            "alumno": alumno,
            "categorias": categorias
        }
    )


# ==========================
# ELIMINAR ALUMNO
# ==========================

def eliminar_alumno(request, id):

    alumno = get_object_or_404(
        Alumno,
        id=id
    )

    alumno.delete()

    return redirect("alumnos")


def importar_excel_view(request):
    if request.method == "POST":
        archivo = request.FILES.get("archivo")
        if not archivo:
            messages.error(
                request,
                "Seleccione un archivo."
            )
            return redirect("importar_excel")
        try:
            df = pd.read_excel(archivo)
            registros = 0
            for _, fila in df.iterrows():
                categoria = Categoria.objects.get(
                    nombre=fila["Categoría"]
                )

                if Alumno.objects.filter(
                    correo=fila["Correo"]
                ).exists():

                    continue

                Alumno.objects.create(
                    nombre=fila["Nombre"],
                    apellido_paterno=fila["Apellido Paterno"],
                    apellido_materno=fila["Apellido Materno"],
                    correo=fila["Correo"],
                    telefono=str(fila["Teléfono"]),
                    fecha_nacimiento=fila["Fecha Nacimiento (AAAA-MM-DD)"],
                    tutor_nombre=fila["Tutor"],
                    tutor_telefono=str(fila["Teléfono Tutor"]),
                    categoria=categoria,
                    status=True
                )

                registros += 1

            messages.success(
                request,
                f"Se importaron {registros} alumnos correctamente."
            )

        except Exception as e:
            messages.error(
                request,
                str(e)
            )

        return redirect("importar_excel")

    return render(
        request,
        "importar_excel.html"
    )