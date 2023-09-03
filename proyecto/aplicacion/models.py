from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    nit = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Garantia(models.Model):
    banco = models.CharField(max_length=50)
    contrato = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=100, decimal_places=2)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()


    def __str__(self):
        return f"Vigencia {self.fecha_inicial}, {self.fecha_final}"
    
class Sucursal(models.Model):
    ciudad = models.CharField(max_length=50)
    cantidad_empleados = models.IntegerField()

    def __str__(self):
        return f"Vigencia {self.ciudad}, {self.cantidad_empleados}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"    
