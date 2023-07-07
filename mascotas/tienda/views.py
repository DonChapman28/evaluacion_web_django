from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto,Marca,Categoria,Carrito,ItemCarrito
from .forms import ProductoForm,MarcaForm,CategoriaForm,CustomUserCreationForm,AgregarProductoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = AgregarProductoForm(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']
            
            carrito, created = Carrito.objects.get_or_create(usuario=request.user)
            item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
            item.cantidad += cantidad
            item.save()
            
            return redirect('ver_carrito')
    else:
        form = AgregarProductoForm()
    
    return render(request, 'agregar_producto.html', {'form': form})

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = carrito.productos.all()
    return render(request, 'ver_carrito.html', {'carrito': carrito, 'items': items})

@login_required
def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    item.delete()
    return redirect('ver_carrito')

#usuarios

#regsitro
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

#carrito
def carrito(request):
    return render(request, 'carrito.html')

