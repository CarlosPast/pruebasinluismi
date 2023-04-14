from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
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

class UsuarioManager(BaseUserManager):
    def create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email válido")
        user = self.model(email=self.normalize_email(email),**extra_fields )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_susperuser", True)
        return self.create_user(email,password,**extra_fields)



class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS = ['username,password']

    objects = UsuarioManager()

    def __str__(self):
        return self.username, self.email