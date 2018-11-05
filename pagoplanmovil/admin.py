from django.contrib import admin
from pagoplanmovil.models import Cliente, Combo, ComboAdmin, Pago, PagoAdmin, Factura

# Register your models here.
admin.site.register(Combo, ComboAdmin)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Pago, PagoAdmin)
# Register your models here.
