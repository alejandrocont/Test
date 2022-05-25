from django.contrib import admin

from BDatos1.gestionPedidos.models import Administrador, Boleta, Clientes, Pedido, Producto

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Administrador)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(Pedido)