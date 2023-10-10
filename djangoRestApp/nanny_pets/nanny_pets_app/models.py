from django.db import models

# Create your models here.

# class Snippet(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     code = models.TextField()
#     linenos = models.BooleanField(default=False)
#     language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
#     style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

#     class Meta:
#         ordering = ['created']

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    foto_perfil = models.ImageField()

    class Meta:
        abstract = True

class Cuidador(Pessoa):
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

class Tutor(Pessoa):
    teste = models.BooleanField(default=False)

class AvaliacaoTutor(models.Model):
    nota = models.IntegerField()
    comentario = models.TextField()
    data_hora = models.DateTimeField()