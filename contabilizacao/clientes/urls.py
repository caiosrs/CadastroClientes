# clientes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar-premium/', views.cadastrar_cliente_premium, name='cadastrar_cliente_premium'),
]
