from .serializer import EstadosSerializers
from .models import CapitaisEstados
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EstadosAPI(APIView):
    """
    API de Estados e Capitais
    """

    def get(self, request):
        dados = CapitaisEstados.objects.all()
        dadosserializer = EstadosSerializers(dados, many=True)
        return Response(dadosserializer.data)

    def post(self, request):
        serializer = EstadosSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
