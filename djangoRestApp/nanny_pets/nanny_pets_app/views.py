from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Cuidador, Caracteristicas, Tutor
from .serializers import TutorSerializer,CuidadorSerializer, CaracteristicasSerializer
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

class TutorAPIView(APIView):
    serializer_class = TutorSerializer

    def get(self, request):
     	tutores = Tutor.objects.all()
     	serializer = TutorSerializer(tutores, many=True)
     	return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

