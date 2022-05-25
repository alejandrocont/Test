from distutils.command.upload import upload
from email.mime import image
from pickle import TRUE
from pickletools import markobject
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Clientes(models.Model):
    idCliente=models.AutoField(primary_key=True, verbose_name='Codigo de Cliente')
    nombreCliente=models.CharField(max_length=30, verbose_name='Nombre del Cliente',null=True,blank=True)
    correoCliente=models.EmailField(verbose_name='Correo del Cliente',null=True,blank=True)
    claveCliente=models.CharField(max_length=20,verbose_name='Clave del Cliente',null=True,blank=True)
    
    def __str__(self) :
        return self.nombreCliente

class Administrador(models.Model):
    idAdmin=models.AutoField(primary_key=True,verbose_name='Codigo de Administrador',null=True,blank=True)
    nombreAdmin=models.CharField(max_length=30,verbose_name='Nombre del Administrador',null=True,blank=True)
    correoAdmin=models.EmailField(verbose_name='Correo del Administrador',null=True,blank=True)
    claveAdmin=models.CharField(max_length=20,verbose_name='Clave del Administrador',null=True,blank=True)

    def __str__(self) :
        return self.nombreAdmin

class Producto(models.Model):
    idProducto=models.AutoField(primary_key=True,verbose_name='Codigo de Producto',null=True,blank=True)
    nombreProducto=models.CharField(max_length=30,verbose_name='Nombre del Producto',null=True,blank=True)
    descripcion=models.CharField(max_length=100,verbose_name='Descripcion del Producto',null=True,blank=True)
    foto=models.ImageField(upload_to="",verbose_name='Foto del Producto',null=True)
    precio=models.IntegerField(verbose_name='Precio del Producto',null=True,blank=True)
    admin=models.ForeignKey(Administrador,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self) :
        return self.nombreProducto


class Pedido(models.Model):
    idPedido=models.IntegerField(primary_key=True)
    fecha=models.DateField(verbose_name='Fecha de Pedido',null=True,blank=True)
    cliente=models.ForeignKey(Clientes,null=True,blank=True,on_delete=models.CASCADE)
    total=models.IntegerField(verbose_name='Total a pagar',null=True,blank=True)

    def __str__(self) :
        return self.total

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True,verbose_name='Numero de registro')
    producto=models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido,null=True,blank=True,on_delete=models.CASCADE)
    cantidad=models.IntegerField(verbose_name='Cantidad de producto',null=True,blank=True)
    subtotal=models.IntegerField(verbose_name='Subtotal a pagar',null=True,blank=True)

    def __str__(self) :
        return self.subtotal