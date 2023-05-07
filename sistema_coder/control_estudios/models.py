from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=64)  # Equivalente de str
    comision = models.IntegerField()  # Equivalent de int
    
    def __str__(self):
        return f"{self.nombre} | {self.comision}"

class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True) #blank=true lo hace no obligatorio
    telefono = models.CharField(max_length=20,blank=True) #en los campos numeros se debe poner null=true
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre}  {self.apellido}"

class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=128)
    bio = models.TextField()
    
    def __str__(self):
        return f"{self.nombre}  {self.apellido}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False)  # equivalente a bool (True, False)
