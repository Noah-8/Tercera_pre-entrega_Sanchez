from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Perro

def inicio(request):
    template = loader.get_template('inicio.html')
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos': segundos,
    }
    renderizar_template = template.render(diccionario)
    return HttpResponse(renderizar_template)

# def fecha_actual(request):
#     fecha = datetime.now()
#     return HttpResponse(f'<h1>Fecha actual: {fecha}</h1>')

def crear_perro(request, nombre, edad):
    template = loader.get_template('crear_perro.html')
    perro = Perro(nombre=nombre, edad=edad)
    perro.save()
    diccionario = {
        'perro': perro,
    }
    renderizar_template = template.render(diccionario)
    return HttpResponse(renderizar_template)