"""ServicioDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static 
from django.conf.urls.static import static
from django.contrib.auth import  views
from AplicacionDjango.views import listadoProducto,registrarProducto,eliminar_producto,modificar_producto,modificar,menu,home2,carrito,cuenta,destacados,perfil,registrarProducto,Sesion,registro3,registro2,PlantillaHome,formulario2,feed,registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.LoginView.as_view(template_name='core/login.html') , name='login'),
    path('logout', views.LogoutView.as_view(template_name='core/logout.html') , name='logout'),
    path('listadoProducto/', listadoProducto,name='listadoProducto'),
    path('agregar_productos/',registrarProducto,name='agregar_producto'),
    path('eliminar_producto/<int:id>',eliminar_producto,name='eliminar_producto'),
    path('modificar_producto/<int:id>',modificar_producto,name='modificar_producto'),
    path('modificar/',modificar,name='modificar'),
    path('menu/',menu , name='menu'),
    path('carrito/',carrito , name='carrito'),
    path('home2/',home2 , name='home2'),
    path('cuenta/',cuenta , name='cuenta'),
    path('destacados/',destacados , name='destacados'),
    path('perfil/',perfil , name='perfil'),
    path('Sesion/',Sesion , name='sesion'),
    path('registro3/',registro3 , name='registro3'),
    path('registro2/',registro2 , name='registro2'),
    path('PlantillaHome/',PlantillaHome , name='PlantillaHome'),
    path('formulario2/',formulario2 , name='formulario2'),
    path('feed/',feed , name='feed'),
    path('registro/',registro , name='registro'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

