
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gestionPedidos.views import listar_producto,registrar_producto,eliminar_producto,modificar_producto,modificar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_producto/', listar_producto,name='listar_producto'),
    path('registrar_productos/',registrar_producto,name='registrar_producto'),
    path('eliminar_producto/<int:id>',eliminar_producto,name='eliminar_producto'),
    path('modificar_producto/<int:id>',modificar_producto,name='modificar_producto'),
    path('modificar/',modificar),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)