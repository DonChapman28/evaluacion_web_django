from django.db import models
from django.contrib.auth.models import AbstractUser, User

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
    
class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')
   

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    

opciones_pago = [
    (0, "Debito"),
    (1, "Credito"),
    (2, "Visa/Nacional"),
    (3, "Visa/Internacional"),
]

class TipoPago(models.Model):
    pago = models.IntegerField(choices=opciones_pago)
    
    
#user

    

    
    
