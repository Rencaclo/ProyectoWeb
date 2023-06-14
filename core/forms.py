from django import forms
from django.forms import ModelForm
from .models import *


# ES EL TEMPLATE DEL FORMULARIO
class ProductoForm(ModelForm):
    class  Meta :
        model = Producto
        fields= '__all__'




