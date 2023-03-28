from django.db import models


class tipoprueba(models.TextChoices):
    MALA = "Mala"
    NORMAL = "Normal"

# Create your models here.
class prueba(models.Model):
    nombre = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    tipo = models.CharField(max_length=30,choices=tipoprueba.choices)
    numero = models.IntegerField()
    fecha_salida = models.DateTimeField()

    def __str__(self):
        return self.nombre

class pruebita(models.Model):
    amount = models.FloatField()
    prueba = models.ForeignKey(prueba, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount) + "y el nombre de la prueba"

class prueba_del_algodon(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre