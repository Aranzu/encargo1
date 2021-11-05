from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Proveedor

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"
        labels = {
            'Nombre': '',
            'Direccion': '',
            'Telefono': '',
            'email': '',
            'Rubro': ''
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'Direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Dirección'}),
            'Telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefono'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'email'}),
            'Rubro': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Rubro'})
        }