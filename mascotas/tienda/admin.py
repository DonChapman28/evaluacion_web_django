from django.contrib import admin
from .models import Marca, Categoria, Producto,Carrito,ItemCarrito,TipoPago

# Register your models here.

admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(TipoPago)


