from django.db import models

class Administrador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)

class SolicitacaoCuidador(models.Model):
    comprovante = models.ImageField
    fotoResidencia = models.ImageField
    statusSolicitacao = models.CharField
    endereco = models.CharField(max_length=100)
    codigo = models.CharField

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.IntegerField(max_length=11)
    endereco = models.CharField(max_length=100)

class Hospedagem(models.Model):
    dataInicio = models.CharField
    dataFinal = models.CharField
    status = models.IntegerField(max_length=100)
    pets = models.IntegerField(max_length=100)
    cuidador = models.CharField(max_length=100)

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(max_length=100)
    porte = models.CharField(max_length=100)
    docil = models.BooleanField
    codigo = models.CharField(max_length=100)

class Cuidador(models.Model):
    diasDisponiveis = models.CharField
    valorDiaria = models.IntegerField
    preferencia = models.CharField(max_length=300)
