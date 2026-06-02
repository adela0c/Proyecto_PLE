from django.db import models

# Create your models here.
class Alumno (models.Model):
    Curso=[
        ('Ingles', 'Frances')
    ]
    Nivel=[
        ('Basico', 'Intermedio', 'Avanzado', 'Certificacion')
    ]
    nombre = models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    edad=models.IntegerField
    sexo=models.CharField(max_length=100)
    categoria=models.CharField(max_length=100)

class Profesores (models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    curso=models.CharField(max_length=100)
    

