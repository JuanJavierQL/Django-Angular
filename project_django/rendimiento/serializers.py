from rest_framework import serializers
from rendimiento.models import Reporte

class RendimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = ('n_id', 's_nombre', 's_parametro', 'b_activo', 'd_fecha_inicio_periodo', 'd_fecha_regitro')