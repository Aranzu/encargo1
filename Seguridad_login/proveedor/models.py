from django.db import models

# Create your models here.
class Proveedor(models.Model):
    IDProveedor = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=11)
    email = models.EmailField()
    Rubro = models.CharField(max_length=20)

    def __str__(self):
        return self.Nombre