from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    
class Articulo(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    
class Pago(models.Model):
    monto = models.IntegerField()