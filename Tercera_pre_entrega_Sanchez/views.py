from django.http import HttpResponse
from django.template import Template, Context

def inicio(request):
    archivo = open(r'C:\Users\Elast\OneDrive\Escritorio\proyectos\Tercera pre-entrega Sanchez\Tercera_pre_entrega_Sanchez\templates\inicio.html', 'r')
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    renderizar_template = template.render(contexto)
    
    return HttpResponse(renderizar_template)