from rest_framework import serializers

from invoice.invoices.models import Cliente as ClienteModel
from invoice.invoices.models import ItemFactura as ItemFacturaModel
from invoice.invoices.models import Factura as FacturaModel
from invoice.invoices.models import Cheque as ChequeModel
from invoice.invoices.models import Tarjeta as TarjetaModel
from invoice.invoices.models import Otros as OtrosModel

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteModel
        fields = ['id', 'nombre', 'direccion', 'telefono', 'correo_electronico', 'nit']
        
class ItemFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFacturaModel
        fields = ['id', 'cantidad', 'descripcion', 'precio_unitario', 'ventas_exentas', 'ventas_gravadas', 'tipo_impuesto']

class FacturaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    items = ItemFacturaSerializer(many=True)
    class Meta:
        model = FacturaModel
        fields = ['id', 'observaciones', 'numero', 'cai', 'rango_facturas', 'fecha_limite_emision', 'fecha', 'cliente', 'items', 'nro_orden_compra_exenta', 'nro_constancia_registro_exonerado', 'nro_registro_sag', 'tipo_pago', 'responsable_factura', 'subtotal_exento', 'subtotal_exonerado', 'subtotal_gravado_15', 'subtotal_gravado_18', 'descuento_rebajas', 'isv_15', 'isv_18', 'total']

class ChequeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChequeModel
        fields = ['id', 'nro_cheque', 'banco']

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjetaModel
        fields = ['id', 'nro_tarjeta', 'tipo_tarjeta']

class OtrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtrosModel
        fields = ['id', 'descripcion', 'monto']
