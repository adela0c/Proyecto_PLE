from django.contrib import admin
from .models import *

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display=(
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'telefono',
        'correo',
        'status'
    )
    search_fields = (
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'correo'
    )
    list_filter = (
        'categoria',
        'status'
    )


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido_paterno',
        'correo',
        'telefono',
        'status'
    )

    search_fields = (
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'correo'
    )

    list_filter = ('status',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre'
    )

    search_fields = (
        'nombre',
    )

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre'
    )

    search_fields = (
        'nombre',
    )

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'monto'
    )

    search_fields = (
        'nombre',
    )
@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'curso',
        'nivel',
        'profesor',
        'periodo'
    )

    search_fields = (
        'nombre',
        'curso__nombre',
        'profesor__nombre'
    )

    list_filter = (
        'curso',
        'nivel',
        'periodo'
    )
@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = (
        'alumno',
        'grupo',
        'fecha_inscripcion'
    )

    search_fields = (
        'alumno__nombre',
        'alumno__apellido_paterno',
        'grupo__nombre'
    )

    list_filter = (
        'grupo',
        'fecha_inscripcion'
    )
@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = (
        'inscripcion',
        'parcial',
        'final',
        'promedio'
    )

    search_fields = (
        'inscripcion__alumno__nombre',
        'inscripcion__alumno__apellido_paterno'
    )

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_documento',
        'alumno',
        'profesor'
    )

    search_fields = (
        'nombre_documento',
    )