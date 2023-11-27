from django.contrib import admin

# Register your models here.

from .models import Cliente, ItemFactura, Factura, Cheque, Tarjeta, Otros

admin.site.register(Cliente)
admin.site.register(ItemFactura)
admin.site.register(Factura)
admin.site.register(Cheque)
admin.site.register(Tarjeta)
admin.site.register(Otros)

