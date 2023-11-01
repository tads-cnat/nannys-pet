from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cuidador, Caracteristicas
from .serializers import CuidadorSerializer, CaracteristicasSerializer
# Create your views here.

class CuidadorAPIView(APIView):

    def get(self, request):
        cuidadores = Cuidador.objects.all()
        serializer = CuidadorSerializer(cuidadores, many=True)
        return Response(serializer.data)

class CaracteristicasAPIView(APIView):

    def get(self, request):
        caracteristicas = Caracteristicas.objects.all()
        serializer = CaracteristicasSerializer(caracteristicas, many=True)
        return Response(serializer.data)