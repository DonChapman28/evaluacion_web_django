from django.urls import path
from .views import base, galeria,productos,marca,categoria,listar_productos,listar_marcas,\
    editar_productos,editar_marcas,eliminar_marcas,eliminar_productos,listar_categorias,\
    editar_categorias,eliminar_categorias,home,registro

urlpatterns = [
    
    path('', home, name="home"),
    path('galeria', galeria, name="galeria"),

    #usuario
    path('registro', registro, name="registro"),

    #administracion
    path('productos', productos, name="productos"),
    path('marca', marca, name="marca"),
    path('categoria', categoria, name="categoria"),

   
    path('listar_productos', listar_productos, name="listar_productos"),
    path('editar_productos/<id>/', editar_productos, name="editar_productos"),
    path('eliminar_productos/<id>/', eliminar_productos, name="eliminar_productos"),

    path('listar_marcas', listar_marcas, name="listar_marcas"),
    path('editar_marcas/<id>/', editar_marcas , name="editar_marcas"),
    path('eliminar_marcas/<id>/', eliminar_marcas, name="eliminar_marcas"),

    path('listar_categorias', listar_categorias, name="listar_categorias"),
    path('editar_categorias/<id>/', editar_categorias, name="editar_categorias"),
    path('eliminar_categorias/<id>/', eliminar_categorias, name="eliminar_categorias"),
]