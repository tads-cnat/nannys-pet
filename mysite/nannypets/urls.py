from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'nannypets'
urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name = 'index'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
]