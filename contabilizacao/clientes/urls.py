# clientes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar-premium/', views.cadastrar_cliente_premium, name='cadastrar_cliente_premium'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('editar-premium/<int:id>/', views.editar_cliente_premium, name='editar_cliente_premium'),
    path('excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
    path('excluir-premium/<int:id>/', views.excluir_cliente_premium, name='excluir_cliente_premium'),
]
