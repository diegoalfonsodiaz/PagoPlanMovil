from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.nombre

class Combo(models.Model):
    nombre = models.CharField(max_length=200)
    monto = models.FloatField()
    def __str__(self):
        return self.nombre

class Pago(models.Model):
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    combos = models.ManyToManyField(Combo, through='Factura')
    montototal = models.FloatField()
    def __str__(self):
        return self.empleado

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)


class FacturaInLine(admin.TabularInline):
    model = Factura
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class ComboAdmin(admin.ModelAdmin):
    inlines = (FacturaInLine,)

class PagoAdmin (admin.ModelAdmin):
    inlines = (FacturaInLine,)