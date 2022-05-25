

# Create your views here.
from django.shortcuts import render, redirect
from .models import Administrador, Mascota, Producto, Raza
from django.contrib import messages
# Create your views here.


def listar_producto(request):
    productos = Producto.objects.all()
    contexto = {"producto":productos}
    return render(request,'core/listadoProductos.html',contexto)

def registrar_producto(request):
    nombre_p = request.POST['nombre']
    descripcion_p = request.POST['descripcion']
    precio_p = request.POST['precio']
    img_foto = request.FILES['foto_p']
    admin_r = request.POST['id_admin']

    admin_p = Administrador.objects.get(idAdmin = admin_r)

    Producto.objects.create(nombreProducto = nombre_p, descripcion = descripcion_p, precio = precio_p, foto = img_foto, admin = admin_p)

    messages.success(request,'Producto Registrado')

    return redirect('formulario_producto')


def eliminar_producto(request, id):
    producto1 = Producto.objects.get( idProducto = id)
    producto1.delete() 

    messages.success(request,'Producto Eliminado')

    return redirect('listado_producto')


def modificar_producto(request, id):
    producto1 = Producto.objects.get( idProducto = id)
    admin1 = Administrador.objects.all()

    contexto = {
        "producto":producto1,
        "admin":admin1 
    }
    return render(request,'core/modificarProducto.html',contexto)



def modificar(request):
    id_p = request.POST['id']
    nombre_p = request.POST['nombre']
    descripcion_p = request.POST['descripcion']
    precio_p = request.POST['precio']
    img_foto = request.FILES['foto_p']
    admin_r = request.POST['id_admin']

    producto = Producto.objects.get(idProducto = id_p) 
    
    producto.idProducto = id_p
    producto.nombreProducto = nombre_p
    producto.descripcion = descripcion_p
    producto.precio = precio_p
    producto.foto = img_foto
    producto.admin = admin_r

    admin_r2 =  Administrador.objects.get(idAdmin = admin_r)

    producto.admin = admin_r2
    producto.save()

    messages.success(request, 'Producto Modificado')
    return redirect('listado_producto')

























