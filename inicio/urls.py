from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cliente/', views.crear_cliente, name='cliente'),
    path('articulos/', views.listar_articulos, name='listar_articulos'),
    path('articulos/agregar/', views.agregar_articulos, name='agregar_articulos'),
    path('pago/', views.realizar_pago, name='pago')
]
