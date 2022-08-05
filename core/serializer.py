from rest_framework import serializers

from .models import CapitaisEstados

class EstadosSerializers(serializers.ModelSerializer):

    class Meta:
        model = CapitaisEstados
        fields = (
            'id', 'estado', 'capital', 'habitantes'
        )