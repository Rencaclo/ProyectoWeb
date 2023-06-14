from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index" ),
    path('about/', about, name="about" ),
    path('cart/', cart, name="cart" ),
    path('checkout/', checkout, name="checkout" ),
    path('contact/', contact, name="contact" ),
    path('productsingle/', productsingle, name="productsingle" ),
    path('shop/', shop, name="shop" ),
    
    #CRUD

    path('agregarproductos/', agregarproductos, name="agregarproductos" ),
    path('actualizar/<id>/', actualizar, name="actualizar" ),
    path('eliminar/<id>/', eliminar, name="eliminar" ),
]
