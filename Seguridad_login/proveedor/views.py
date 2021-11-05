from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.

def add_proveedor(request):
    registrado = False
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_proveedor?registrado=True')
    else:
        form = ProveedorForm
        if 'registrado' in request.GET:
            registrado = True
    return render(request, 'add_proveedor.html', {'form': form, 'registrado':registrado})

def list_proveedor(request):
    proveedor_list = Proveedor.objects.all()
    return render(request, 'list_proveedor.html', {'proveedor_list':proveedor_list})

def show_proveedor(request, IDProveedor):
    proveedor = Proveedor.objects.get(pk=IDProveedor)
    return render(request, 'show_proveedor.html', {'proveedor':proveedor})