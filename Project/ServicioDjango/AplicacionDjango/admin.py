from django.contrib import admin

from AplicacionDjango.models import Rol, Boleta, Usuario, Pedido, Producto

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(Pedido)
