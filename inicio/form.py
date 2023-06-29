from django import forms

class CrearClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class AgregarArticuloFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    
class BuscarArticuloFormulario(forms.Form):
    modelo = forms.CharField(max_length=20, required=False)
    
class PagoFormulario(forms.Form):
    monto = forms.IntegerField()