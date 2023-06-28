from django.db import models

class Administrador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)

class SolicitacaoCuidador(models.Model):
    comprovante = models.ImageField
    foto_residencia = models.ImageField
    status_solicitacao = models.CharField
    endereco = models.CharField(max_length=100)
    codigo = models.CharField

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)

class Hospedagem(models.Model):
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    status = models.IntegerField(max_length=100)
    pets = models.IntegerField(max_length=100)
    cuidador = models.CharField(max_length=100)

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(max_length=100)
    porte = models.CharField(max_length=100)
    caracteristica = models.CharField(max_length=300)

class Cuidador(models.Model):
    dias_disponiveis = models.CharField
    valor_diaria = models.IntegerField
    preferencia = models.CharField(max_length=300)
    
