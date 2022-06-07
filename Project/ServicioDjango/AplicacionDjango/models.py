from distutils.command.upload import upload
from email.mime import image
from hashlib import blake2b
from pickle import TRUE
from pickletools import markobject
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Rol(models.Model):
    idRol=models.AutoField(primary_key=True, verbose_name='Codigo de Rol')
    nombreRol=models.CharField(max_length=30, verbose_name='Nombre del Rol',null=True,blank=True)
    
    def __str__(self) :
        return self.nombreRol

class Usuario(models.Model):
    idUsuario=models.AutoField(primary_key=True,verbose_name='Codigo de Usuario',null=False,blank=True)
    nombreUsuario=models.CharField(max_length=30,verbose_name='Nombre del Usuario',null=True,blank=True)
    correoUsuario=models.EmailField(verbose_name='Correo del Usuario',null=True,blank=True)
    claveUsuario=models.CharField(max_length=20,verbose_name='Clave del Usuario',null=True,blank=True)
    rol= models.ForeignKey(Rol,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self) :
        return self.nombreUsuario

class Producto(models.Model):
    idProducto=models.AutoField(primary_key=True,verbose_name='Codigo de Producto',null=False,blank=True)
    nombreProducto=models.CharField(max_length=30,verbose_name='Nombre del Producto',null=True,blank=True)
    descripcion=models.TextField(max_length=100,verbose_name='Descripcion del Producto',null=True,blank=True)
    foto=models.ImageField(upload_to="imagenes/",verbose_name='Foto del Producto',null=True)
    precio=models.IntegerField(verbose_name='Precio del Producto',null=True,blank=True)
    categoria = models.CharField(max_length=20, verbose_name='Categoria del Producto', null=True, blank=True )
    

    def __str__(self) :
        return self.nombreProducto

class Pedido(models.Model):
    idPedido=models.IntegerField(primary_key=True)
    fecha=models.DateField(verbose_name='Fecha de Pedido',null=True,blank=True)
    cliente=models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    total=models.IntegerField(verbose_name='Total a pagar',null=True,blank=True)


class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True,verbose_name='Numero de registro')
    producto=models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido,null=True,blank=True,on_delete=models.CASCADE)
    cantidad=models.IntegerField(verbose_name='Cantidad de producto',null=True,blank=True)
    subtotal=models.IntegerField(verbose_name='Subtotal a pagar',null=True,blank=True)

