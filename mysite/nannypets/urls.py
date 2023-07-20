from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
""" from django.conf.urls.static import static
from django.conf import settings """

app_name = 'nannypets'
urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name = 'index'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('pets/',login_required(views.PetsView.as_view()), name = 'pets'),
    path('pets/<int:pk>/',login_required(views.PetView.as_view()), name = 'pet'),
    path('minhas_solicitacoes/', login_required(views.SolicitacaoHospedagemView.as_view()), name = 'listar_solicitacoes'),
    path('hospedagem/', login_required(views.HospedagemView.as_view()), name = 'hospedagem'),
]
""" urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """