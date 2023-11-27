from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import ChequeSerializer, ClienteSerializer, FacturaSerializer, ItemFacturaSerializer, OtrosSerializer, TarjetaSerializer
from .serializers import ChequeModel, ClienteModel, FacturaModel, ItemFacturaModel, OtrosModel, TarjetaModel

class ClienteViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = "identificacion"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(identificacion=self.request.identificacion)

class ItemFacturaViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = ItemFacturaModel.objects.all()
    serializer_class = ItemFacturaSerializer
    

class FacturaViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = FacturaModel.objects.all()
    serializer_class = FacturaSerializer

class ChequeViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = ChequeModel.objects.all()
    serializer_class = ChequeSerializer

class TarjetaViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = TarjetaModel.objects.all()
    serializer_class = TarjetaSerializer

class OtrosViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = OtrosModel.objects.all()
    serializer_class = OtrosSerializer

    @action(detail=True, methods=['post'])
    def add(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(factura_id=pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
