from django.urls import path

<<<<<<< HEAD
from .views import CaracteristicasAPIView,CaracteristicasDoCuidadorView, CuidadorAPIView, TutorAPIView,CuidadorFiltradoView
=======
from .views import CaracteristicasAPIView, CuidadorAPIView, TutorAPIView
>>>>>>> 9fc74eeffb0b0f50649d41943c2720a3f24d7d30

urlpatterns = [
    path('cuidadores/', CuidadorAPIView.as_view(), name='cuidadores'),
    path('caracteristicas/', CaracteristicasAPIView.as_view(), name='caracteristicas'),
    path('tutores/',TutorAPIView.as_view(), name='tutores'),
    path('cuidadores/<int:cuidador_id>/caracteristicas/',CaracteristicasDoCuidadorView.as_view(), name='caracteristicascuidador'),
    path('cuidadores-filtrados/', CuidadorFiltradoView.as_view(), name='cuidadores-filtrados'),
]