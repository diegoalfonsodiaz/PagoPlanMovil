from django.shortcuts import render
#librería para manejar el envío de mensajes
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ClienteForm, ComboForm, PagoForm
from pagoplanmovil.models import Cliente, Combo, Pago, Factura
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            #post.published_date = timezone.now()
            post.save()
            return redirect('cliente_detail', pk=post.pk)
    else:
        form = ClienteForm()
    return render(request, 'pagoplanmovil/cliente_edit.html', {'form': form})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'pagoplanmovil/cliente_list.html', {'clientes': clientes})


def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'pagoplanmovil/cliente_detail.html', {'cliente': cliente})

@login_required
def cliente_remove(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('cliente_list')

@login_required
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('cliente_detail', pk=post.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'pagoplanmovil/cliente_edit.html', {'form': form})


#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------


def combo_list(request):
    combos = Combo.objects.all()
    return render(request, 'pagoplanmovil/combo_list.html', {'combos': combos})

def combo_detail(request, pk):
    combo = get_object_or_404(Combo, pk=pk)
    return render(request, 'pagoplanmovil/combo_detail.html', {'combo': combo})


@login_required
def combo_new(request):
    if request.method == "POST":
        form = ComboForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            #post.published_date = timezone.now()
            post.save()
            return redirect('combo_detail', pk=post.pk)
    else:
        form = ComboForm()
    return render(request, 'pagoplanmovil/combo_edit.html', {'form': form})

@login_required
def combo_edit(request, pk):
    combo = get_object_or_404(Combo, pk=pk)
    if request.method == "POST":
        form = ComboForm(request.POST, instance=combo)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('combo_detail', pk=combo.pk)
    else:
        form = ComboForm(instance=combo)
    return render(request, 'pagoplanmovil/combo_edit.html', {'form': form})

@login_required
def combo_remove(request, pk):
    combo = get_object_or_404(Combo, pk=pk)
    combo.delete()
    return redirect('combo_list')


#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

def pago_list(request):
    pagos = Pago.objects.all()
    return render(request, 'pagoplanmovil/pago_list.html', {'pagos': pagos})

@login_required
def pago_new(request):
    if request.method == "POST":
        formulario = PagoForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            user = User.objects.get(username=request.user.username)
            post.empleado=user
            post.save()
            for cliente_id in request.POST.getlist('cliente'):
                for combo_id in request.POST.getlist('combos'):
                    factura = Factura(combo_id=combo_id, pago_id = user.id,cliente_id=cliente_id)
                    factura.save()
                    return redirect('factura_list')


            messages.add_message(request, messages.SUCCESS, 'Pago Guardado Exitosamente')
    else:
        formulario = PagoForm()
    return render(request, 'pagoplanmovil/pago_new.html', {'formulario': formulario})


#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

def factura_list(request):
    facturas = Factura.objects.all()
    return render(request, 'pagoplanmovil/factura_list.html', {'facturas': facturas})