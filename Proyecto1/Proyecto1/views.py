from fileinput import close
from multiprocessing import context
from pipes import Template
from re import TEMPLATE
from django.http import HttpResponse
from django.template import Template, Context

def respuesta(request):

    doc_externo=open("C:/Users/User/Desktop/duoc/diseño web/ProyectosDjango/Proyecto1/Proyecto1/Plantillas/plantilla1.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("adios")