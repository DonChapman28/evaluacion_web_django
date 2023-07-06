from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoría = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    descripción = models.TextField()
    precioCosto = models.IntegerField()
    precioVenta = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre
    

    
    
