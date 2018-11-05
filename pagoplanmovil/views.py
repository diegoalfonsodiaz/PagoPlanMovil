from django.shortcuts import render
#librería para manejar el envío de mensajes
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ClienteForm
from pagoplanmovil.models import Cliente, Combo, Pago, Factura
from django.shortcuts import redirect

# Create your views here.
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

def cliente_remove(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('cliente_list')


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