from django.urls import path
from pedido_app import views

urlpatterns = [
    path('Pedido', views.inicio_vistaPedido, name="Pedido"),
    path("registrarPedido/", views.registrarPedido, name="registrarPedido"),
    path("seleccionarPedido/<id_pedido>", views.seleccionarPedido, name="seleccionarPedido"),
    path("editarPedido/", views.editarPedido, name="editarPedido"),
    path("borrarPedido/<id_pedido>", views.borrarPedido, name="borrarPedido"),
]
