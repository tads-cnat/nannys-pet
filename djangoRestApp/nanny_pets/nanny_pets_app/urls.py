from django.urls import path

from .views import CaracteristicasAPIView, CuidadorAPIView, TutorAPIView

urlpatterns = [
    path('cuidadores/', CuidadorAPIView.as_view(), name='cuidadores'),
    path('caracteristicas/', CaracteristicasAPIView.as_view(), name='caracteristicas'),
    path('tutores/',TutorAPIView.as_view(), name='tutores'),
]