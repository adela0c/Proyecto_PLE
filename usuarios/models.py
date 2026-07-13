from django.db import models

# Create your models here.
from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"


class Nivel(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()

    tutor_nombre = models.CharField(max_length=150, blank=True, null=True)
    tutor_telefono = models.CharField(max_length=15, blank=True, null=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    status = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='alumnos/',blank=True,null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)  # Inglés / Francés

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    nivel = models.ForeignKey(Nivel, on_delete=models.PROTECT)

    periodo = models.CharField(max_length=50)
    # "Mayo-Agosto 2026"

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    nombre = models.CharField(max_length=50)
    # "Inglés A", "Francés B"

    def __str__(self):
        return f"{self.curso.nombre} - {self.nombre}"

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    grupo = models.ForeignKey(
    Grupo,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno} - {self.grupo}"

class Calificacion(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)

    parcial = models.DecimalField(max_digits=5, decimal_places=2)
    final = models.DecimalField(max_digits=5, decimal_places=2)
    promedio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.inscripcion)

class Documento(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=True, blank=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)

    nombre_documento = models.CharField(max_length=150)
    archivo = models.FileField(upload_to='documentos/')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_documento


    

