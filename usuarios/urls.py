from django.urls import path
from . import views

urlpatterns = [

    # LOGIN
    path("", views.login_view, name="login"),
    path("login/", views.login_view, name="login"),

    # DASHBOARD
    path("inicio/", views.inicio_view, name="inicio"),

    # ALUMNOS
    path("alumnos/", views.alumnos_view, name="alumnos"),
    path("agregar/", views.agregar_view, name="agregar"),

    path(
        "alumno/editar/<int:id>/",
        views.editar_alumno,
        name="editar_alumno"
    ),

    path(
        "alumno/eliminar/<int:id>/",
        views.eliminar_alumno,
        name="eliminar_alumno"
    ),

    # DOCUMENTOS
    path("subir/", views.subir_view, name="subir"),

    # ALUMNO
    path("niveles/", views.niveles_view, name="niveles"),
    path("parcial/", views.parcial_view, name="parcial"),

    path(
    "importar-excel/",
    views.importar_excel_view,
    name="importar_excel"
),

]