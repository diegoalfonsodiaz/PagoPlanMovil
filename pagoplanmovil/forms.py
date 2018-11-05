from django import forms

from .models import Cliente, Combo, Pago, Factura

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'numero', 'email',)

class ComboForm(forms.ModelForm):
    class Meta:
        model = Combo
        fields = ('nombre', 'monto',)

class PagoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Pago
        fields = ('empleado','cliente','fecha','combos','montototal')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.



def __init__ (self, *args, **kwargs):
    super(PagoForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

    self.fields["combos"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget
    self.fields["combos"].help_text = "Ingrese los combos a pagar"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

    self.fields["combos"].queryset = Combo.objects.all()