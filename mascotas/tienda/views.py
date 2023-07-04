from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto,Marca,Categoria
from .forms import ProductoForm,MarcaForm,CategoriaForm


# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'home.html', data)

def galeria(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'galeria.html', data)

#administracion
#agregar
def productos(request):   
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Datos guardados"
        else:   
            data["form"] = formulario
    return render(request, 'administracion/productos.html', data)

def marca(request):
    data = {
        'form': MarcaForm()
    }

    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Datos guardados"
        else:   
            data["form"] = formulario
    return render(request, 'administracion/marca.html', data)

def categoria(request):
    data = {
        'form': CategoriaForm()
    }

    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Datos guardados"
        else:   
            data["form"] = formulario
    return render(request, 'administracion/categoria.html', data)

#listar
def listar_productos(request):
    productos = Producto.objects.all()
    data = {
            'productos': productos
    }
    return render(request, 'administracion/listar_productos.html', data)

def listar_marcas(request):
    marcas = Marca.objects.all()
    data = {
            'marcas': marcas
    }
    return render(request, 'administracion/listar_marcas.html', data)

def listar_categorias(request):
    categorias = Categoria.objects.all()
    data = {
            'categorias': categorias
    }
    return render(request, 'administracion/listar_categorias.html', data)

#editar
def editar_productos(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Datos modificados"
            return redirect('listar_productos')
        else:   
            data["form"] = formulario

    return render(request, 'administracion/editar_productos.html',data)

def editar_marcas(request, id):

    producto = get_object_or_404(Marca, id=id)

    data = {
        'form': MarcaForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Datos modificados"
            return redirect('listar_marcas')
        else:   
            data["form"] = formulario

    return render(request, 'administracion/editar_marcas.html',data)

def editar_categorias(request, id):

    producto = get_object_or_404(Categoria, id=id)

    data = {
        'form': MarcaForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Datos modificados"
            return redirect('listar_categorias')
        else:   
            data["form"] = formulario

    return render(request, 'administracion/editar_categorias.html',data)

#eliminar
def eliminar_productos(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')

def eliminar_marcas(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    return redirect('listar_marcas')

def eliminar_categorias(request, id):
    marca = get_object_or_404(Categoria, id=id)
    marca.delete()
    return redirect('listar_categorias')

#carrito

#usuarios

