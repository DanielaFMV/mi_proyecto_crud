from django.db import models


class Cliente(models.Model):
    nombre         = models.CharField(max_length=100)
    apellido       = models.CharField(max_length=100)
    email          = models.EmailField(unique=True)
    telefono       = models.CharField(max_length=20, blank=True)
    direccion      = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
