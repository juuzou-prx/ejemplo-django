from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def rol_cliente_default():
    rol, _ = Rol.objects.get_or_create(nombre='Cliente')
    return rol.id

class Rol(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.RESTRICT,
                            default=rol_cliente_default)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.rol.nombre}"