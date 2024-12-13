from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'is_active', 'is_staff']


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'total', 'address', 'is_paid']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ingrese la dirección'}),
            'total': forms.NumberInput(attrs={'placeholder': 'Ingrese el total'}),
        }