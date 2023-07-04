from django.urls import path
from . import views

app_name = 'nannypets'
urlpatterns = [
    path('nannypets/', views.IndexView.as_view(), name = 'index'),
]