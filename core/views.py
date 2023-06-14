from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def cart(request):
    return render(request, 'core/cart.html')

def checkout(request):
    return render(request, 'core/checkout.html')

def contact(request):
    return render(request, 'core/contact.html')
    
def productsingle(request):
    return render(request, 'core/productsingle.html')
    
def shop(request):
    productosAll= Producto.objects.all()
    data={

        'listaProductos': productosAll
    }

    return render(request, 'core/shop.html',data)


#CRUD

def agregarproductos(request):
    data={

       'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST) # RECIBE EL CONTENIDO DEL FORMULARIO

        if formulario.is_valid():
            formulario.save()
            data['msj'] = "Producto almacenado correctamente"
            
    return render(request, 'core/agregarproductos.html', data)

def actualizar(request, id):
    producto = Producto.objects.get(id=id)
    data={

       'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto) # RECIBE EL CONTENIDO DEL FORMULARIO

        if formulario.is_valid():
            formulario.save()
            data['msj'] = "Producto actualizado correctamente"
        data['form'] = formulario
            
    return render(request, 'core/actualizar.html', data)

def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.eliminar()

    return redirect(to="shop")
