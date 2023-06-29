from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Cliente, Articulo, Pago
from django.shortcuts import render
from inicio.form import CrearClienteFormulario, AgregarArticuloFormulario, BuscarArticuloFormulario, PagoFormulario



def inicio(request):
    return render(request, 'inicio/inicio.html')



def crear_cliente(request):
    if request.method =="POST":
        formulario = CrearClienteFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente = Cliente(nombre=info['nombre'], edad=info['edad'])
            cliente.save()
        return render(request, 'inicio/crear_cliente.html', {'formulario': formulario})
            
    formulario = CrearClienteFormulario()
    return render(request, 'inicio/crear_cliente.html', {'formulario': formulario})



def agregar_articulos(request):
    if request.method =="POST":
        formulario = AgregarArticuloFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            articulo = Articulo(marca=info['marca'], modelo=info['modelo'])
            articulo.save()
        return render(request, 'inicio/agregar_articulos.html', {'formulario': formulario})
            
    formulario = AgregarArticuloFormulario()
    return render(request, 'inicio/agregar_articulos.html', {'formulario': formulario})



def listar_articulos(request):
    formulario = BuscarArticuloFormulario(request.GET)
    if formulario.is_valid():
        modelo_a_buscar = formulario.cleaned_data['modelo']
        listado_de_articulos = Articulo.objects.filter(modelo__icontains=modelo_a_buscar)
    return render(request, 'inicio/listar_articulos.html', {'formulario': formulario, 'articulos': listado_de_articulos})



def realizar_pago(request):
    if request.method =="POST":
        formulario = PagoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            pago = Pago(monto=info['monto'])
        return render(request, 'inicio/pagar.html', {'formulario': formulario})
            
    formulario = PagoFormulario()
    return render(request, 'inicio/pagar.html', {'formulario': formulario})
