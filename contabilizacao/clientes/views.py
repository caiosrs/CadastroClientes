from django.shortcuts import render, redirect, get_object_or_404
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

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('home')

def excluir_cliente_premium(request, id):
    cliente_premium = get_object_or_404(ClientePremium, id=id)
    cliente_premium.delete()
    return redirect('home')

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cadastrar_cliente.html', {'form': form})

def editar_cliente_premium(request, id):
    cliente_premium = get_object_or_404(ClientePremium, id=id)
    if request.method == 'POST':
        form = ClientePremiumForm(request.POST, instance=cliente_premium)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientePremiumForm(instance=cliente_premium)
    return render(request, 'clientes/cadastrar_cliente_premium.html', {'form': form})