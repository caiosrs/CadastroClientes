# clientes/views.py

from django.shortcuts import render, redirect
from .models import Cliente, ClientePremium
from .forms import ClienteForm, ClientePremiumForm

def home(request):
    clientes = Cliente.objects.all()
    clientes_premium = ClientePremium.objects.all()
    return render(request, 'clientes/home.html', {'clientes': clientes, 'clientes_premium': clientes_premium})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastrar_cliente.html', {'form': form})

def cadastrar_cliente_premium(request):
    if request.method == 'POST':
        form = ClientePremiumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientePremiumForm()
    return render(request, 'clientes/cadastrar_cliente_premium.html', {'form': form})