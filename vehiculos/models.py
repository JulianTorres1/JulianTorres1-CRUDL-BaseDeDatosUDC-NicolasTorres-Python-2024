from django.db import models

class Vehiculo(models.Model):
    num_bastidor = models.CharField(max_length=50, primary_key=True)
    nombre_modelo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    potencia_fiscal = models.IntegerField()
    cilindrada = models.IntegerField()
    en_stock = models.BooleanField()
    id_concesionario = models.IntegerField()
    id_servicio = models.IntegerField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_modelo

