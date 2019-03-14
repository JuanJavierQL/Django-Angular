from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from rendimiento.models import Reporte
from rendimiento.serializers import RendimientoSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

# @csrf_exempt
# def get_data(request):
# 	data = Reporte.objects.all()
# 	serializer = RendimientoSerializer(data, many=True)
# 	return JsonResponse(serializer.data, safe=False)

class ReporteList(generics.ListCreateAPIView):
	queryset = Reporte.objects.all()
	serializer_class = RendimientoSerializer
    