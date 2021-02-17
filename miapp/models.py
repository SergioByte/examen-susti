from django.db import models

# Create your models here.
class Region(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    name = models.CharField(max_length=20, verbose_name="Nombre")
    image = models.ImageField(default='null', verbose_name="Miniatura", upload_to="regiones")
    cases = models.CharField(max_length=10, verbose_name="Casos")
    deaths = models.CharField(max_length=10, verbose_name="Muertes")
    cases = models.CharField(max_length=10, verbose_name="Casos")
    estado = models.CharField(max_length= 1, verbose_name="Estado")      
    lethality = models.CharField(max_length=4, verbose_name="Letalidad")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Editado")
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"
class Employee(models.Model):
    fullname = models.CharField(max_length=50, verbose_name="Nombre Completo")
    job = models.CharField(max_length=30, verbose_name="Trabajo")
    image = models.ImageField(default='null', verbose_name="Identificacion", upload_to="empleados")
    estado = models.CharField(max_length= 1, verbose_name="Estado")      
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Editado")
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

