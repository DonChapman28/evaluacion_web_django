from django import forms
from .models import Producto,Marca,Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

#usuario
opciones_region = [
    [0, "Región de Arica y Parinacota"],
    [1, "Región de Tarapacá"],
    [2, "Región de Antofagasta"],
    [3, "Región de Atacama"],
    [4, "Región de Coquimbo"],
    [5, "Región de Valparaíso"],
    [6, "Región Metropolitana"],
    [7, "Región de O'Higgins"],
    [8, "Región del Maule"],
    [9, "Región del Ñuble"],
    [10, "Región del Biobío"],
    [11, "Región de La Araucanía"],
    [12, "Región de Los Ríos"],
    [13, "Región de Los Lagos"],
    [14, "Región de Aysén"],
    [15, "Región de Magallanes"],
]

opciones_educacion = [
    [0, "Magister"],
    [1, "Doctor"],
    [2, "Profesional"],
    [3, "Otro"],
]

class CustomUserCreationForm(UserCreationForm):
   
    rut = forms.IntegerField()
    dv = forms.CharField(max_length=1)
    fecha_Nacimiento = forms.DateField()
    region = forms.IntegerField(widget=forms.Select(choices=opciones_region))
    telefono = forms.CharField(max_length=15)
    nivel_Educacion = forms.IntegerField(widget=forms.Select(choices=opciones_educacion))
    class Meta:
        model = User
        fields = ('rut','dv','first_name','last_name','fecha_Nacimiento','email','region','telefono','nivel_Educacion','username','password1', 'password2')

