
from itertools import product
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Usuario, Rol, Producto, Pedido, Boleta
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout




def listadoProducto(request):
    productos = Producto.objects.all()
    contexto = {"producto":productos}
    return render(request,'core/listadoProductos.html',contexto)

def registrarProducto(request):
    nombre_p = request.POST['nombre']
    descripcion_p = request.POST['descripcion']
    precio_p = request.POST['precio']
    img_foto = request.FILES['foto_p']
    categoria_p = request.POST['categoria']

    Producto.objects.create(nombreProducto = nombre_p, descripcion = descripcion_p,foto = img_foto, precio = precio_p,  categoria = categoria_p)

    messages.success(request,'Producto Registrado')

    return redirect('registrarProducto')

def eliminar_producto(request, id):
    producto1 = Producto.objects.get( idProducto = id)
    producto1.delete() 

    messages.success(request,'Producto Eliminado')

    return redirect('listadoProducto.html')

def modificar_producto(request, id):
    producto1 = Producto.objects.get( idProducto = id)
    contexto = {
        "producto":producto1, 
    }
    return render(request,'core/modificarProducto.html',contexto)


def modificar(request):
    id_p = request.POST['id']
    nombre_p = request.POST['nombre']
    descripcion_p = request.POST['descripcion']
    img_foto = request.FILES['foto_p']
    precio_p = request.POST['precio']
    categoria = request.POST['categoria']

    producto = Producto.objects.get(idProducto = id_p) 
    
    producto.nombreProducto = nombre_p
    producto.descripcion = descripcion_p
    producto.precio = precio_p
    producto.foto = img_foto
    producto.categoria = categoria

    producto.save()

    messages.success(request, 'Producto Modificado')
    return redirect('listadoProducto')

def menu(request):
    prodpasta = Producto.objects.filter(categoria = "Pasta")
    prodpizza = Producto.objects.filter(categoria = "Pizza")
    prodstarter = Producto.objects.filter(categoria = "Starter")
    contexto = {
        "pizza": prodpizza,
        "pasta": prodpasta,
        "star": prodstarter
    }

    return render(request,'core/menu.html',contexto)

def home2(request):
    usuarios = Usuario.objects.all()
    roles = Rol.objects.all()
    contexto = {"usuarios": usuarios, "roles": roles}
    return render(request,'core/home2.html',contexto)



def carrito(request):
    productos = Producto.objects.all()
    usuarios = Usuario.objects.all()
    boletas = Boleta.objects.all()
    context = {'boletas': boletas, 'productos': productos, 'usuarios': usuarios}
    return redirect(request, 'carrito',context)


def cuenta(request):
    items = Pedido.objects.all()   
    contexto = {'pedido': items}
    return render(request, 'cuenta.html', contexto)


def destacados(request):
    product = Producto.objects.all()
    context = {'product': product}
    return render(request,'destacados.html',context)


def formulario2(request):
    producto = Producto.objects.all()
    contexto = {'producto': producto}
    return render(request,'formulario2.html',contexto)

def perfil(request):
    posts = posts.objects.all()
    usuarios = Usuario.objects.all()
    context = {'posts': posts, 'usuarios': usuarios}
    return render(  request, 'core/perfil.html', context)

def registro2(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuario Registrado')
            return redirect(perfil)
    else:
        form = UserRegisterForm()

    context = {'form': form }
    return render(request, 'core/registro2.html', context)

def logout(request):
    logout(request)
    return render(request,'logout.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'perfil.html')
    else:
        return render(request,'feed.html')

def registro3(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuario Registrado')
            return redirect(perfil)
    else:
        form = UserRegisterForm()

    context = {'form': form }
    return render(request, 'core/registro2.html', context)

def PlantillaHome(request):
    usuarios = Usuario.objects.all()
    roles = Rol.objects.all()
    contexto = {"usuarios": usuarios, "roles": roles}

    return render(request,'core/Plantillahome.html',contexto)

def feed(request):

    return render(request,'feed.html')

def Sesion(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'perfil.html')
    else:
        return render(request,'feed.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuario Registrado')
            return redirect(perfil)
    else:
        form = UserRegisterForm()

    context = {'form': form }
    return render(request, 'core/registro2.html', context)

    return render(request,'registro.html')