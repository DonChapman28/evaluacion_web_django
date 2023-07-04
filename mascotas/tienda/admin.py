from django.contrib import admin
from .models import Marca, Categoria, Producto

# Register your models here.

admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Categoria)