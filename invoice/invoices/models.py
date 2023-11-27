import uuid
from django.db import models

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255, blank=True).null
    rtn = models.CharField(max_length=15, blank=True).null

class ItemFactura(models.Model):
    ISV_15 = '15'
    ISV_18 = '18'
    TIPO_IMPUESTO_CHOICES = [
        (ISV_15, '15%'),
        (ISV_18, '18%'),
    ]
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    ventas_exentas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ventas_gravadas = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_impuesto = models.CharField(max_length=50, choices=TIPO_IMPUESTO_CHOICES, default=ISV_15)

class Factura(models.Model):
    EFECTIVO = 'E'
    CHEQUE = 'C'
    TARJETA = 'T'
    OTROS = 'O'
    TIPO_PAGO_CHOICES = [
        (EFECTIVO, 'Efectivo'),
        (CHEQUE, 'Cheque'),
        (TARJETA, 'Tarjeta'),
        (OTROS, 'Otros'),
    ]
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    observaciones = models.TextField()
    numero = models.CharField(max_length=20)
    cai = models.CharField(max_length=50)
    rango_facturas = models.CharField(max_length=50)
    fecha_limite_emision = models.DateField()
    fecha = models.DateField(auto_created=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemFactura)
    nro_orden_compra_exenta = models.CharField(max_length=20, blank=True).null
    nro_constancia_registro_exonerado = models.CharField(max_length=20, blank=True).null
    nro_registro_sag = models.CharField(max_length=20, blank=True).null
    tipo_pago = models.CharField(max_length=1, choices=TIPO_PAGO_CHOICES, default=EFECTIVO)
    responsable_factura = models.CharField(max_length=255, blank=True).null
    subtotal_exento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal_exonerado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal_gravado_15 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal_gravado_18 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descuento_rebajas = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    isv_15 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    isv_18 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Cheque(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    nro_cheque = models.CharField(max_length=20)
    banco = models.CharField(max_length=50)

class Tarjeta(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    nro_tarjeta = models.CharField(max_length=20)
    
class Otros(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
