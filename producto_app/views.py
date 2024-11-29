from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def inicio_vistaProducto(request):
    losproductos = Producto.objects.all()
    return render(request, 'gestionarProducto.html', {'misproductos': losproductos})

def registrarProducto(request):
    id_producto = request.POST["numidproducto"]
    nombre = request.POST["txtnombre"]
    marca = request.POST["txtmarca"]
    tipo = request.POST["txttipo"]
    volumen = request.POST["numvolumen"]
    precio = request.POST["numprecio"]
    notas_olfativas = request.POST["txtnotas"]

    Producto.objects.create(
        id_producto=id_producto, 
        nombre=nombre, 
        marca=marca, 
        tipo=tipo, 
        volumen=volumen, 
        precio=precio, 
        notas_olfativas=notas_olfativas
    )

    return redirect('Producto')

def seleccionarProducto(request, id_producto):
    try:
        producto = Producto.objects.get(id_producto=id_producto)
        return render(request, "editarProducto.html", {"misproductos": producto})
    except Producto.DoesNotExist:
        return redirect('Producto')  # Redirigir si el producto no se encuentra

def editarProducto(request):
    if request.method == "POST":
        id_producto = request.POST.get("numidproducto")
        nombre = request.POST.get("txtnombre")
        marca = request.POST.get("txtmarca")
        tipo = request.POST.get("txttipo")
        volumen = request.POST.get("numvolumen")
        precio = request.POST.get("numprecio")
        notas_olfativas = request.POST.get("txtnotas")

        try:
            producto = Producto.objects.get(id_producto=id_producto)
            producto.nombre = nombre
            producto.marca = marca
            producto.tipo = tipo
            producto.volumen = volumen
            producto.precio = precio
            producto.notas_olfativas = notas_olfativas
            producto.save()
        except Producto.DoesNotExist:
            return redirect('Producto')  # O manejar el error según lo necesites

    return redirect('Producto')

def borrarProducto(request, id_producto):
    try:
        producto = Producto.objects.get(id_producto=id_producto)
        producto.delete()
    except Producto.DoesNotExist:
        pass  # No hacer nada si no existe, podrías redirigir a un mensaje de error

    return redirect('Producto')
