from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View, generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .forms import SolicitacaoHospedagemForm, PetForm


from .models import User, UserManager, BaseUserManager, Pet, Cuidador, SolicitacaoHospedagem, Hospedagem 

class IndexView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        contexto = {'user':user}
        return render (request, 'nannypets/index.html', contexto)
    
class PetsView(View):
    def get(self, request, *args, **kwargs):
        lista_pets = Pet.objects.filter(user=request.user)
        form = PetForm()
        contexto = {'pets_list':lista_pets, 'form': form}
        return render(request, 'nannypets/pets.html', contexto)
    
    def post(self, request):
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            newpet = form.save(commit=False)
            newpet.user = request.user  
            newpet.save()
            return redirect('nannypets:pets') 
        return render(request, 'nannypets/pets.html', {'form': form})


class HospedagemView(View):
    def get(self, request):
        form = SolicitacaoHospedagemForm(user=request.user)
        return render(request, 'nannypets/hospedagem.html', {'form': form})

    def post(self, request):
        form = SolicitacaoHospedagemForm(request.POST,)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.user = request.user  
            solicitacao.save()
            return redirect('/') 
        return render(request, 'nannypets/hospedagem.html', {'form': form})

class SolicitacaoHospedagemView(View):
    def get(self, request, *args, **kwargs):
        lista_solicitacoes = SolicitacaoHospedagem.objects.filter(cuidador=request.user.cuidador)
        contexto = {'solicitacao_list':lista_solicitacoes}
        return render(request, 'nannypets/lista_solicitacoes.html', contexto)
        
    
def cadastro(request):
    if request.method == "GET":
        return render(request, 'nannypets/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        first_name = request.POST.get('username')
        last_name = request.POST.get('last_name')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("Já existe um usuário com esse nome!")
        
        user = User.objects.create_user(username=username, email=email, password=senha, first_name=first_name, last_name= last_name)
        user.save()

        return HttpResponseRedirect('/accounts/login')


