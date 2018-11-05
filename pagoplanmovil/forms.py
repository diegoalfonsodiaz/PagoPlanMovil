from django import forms

from .models import Cliente, Combo, Pago, Factura

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'numero', 'email',)