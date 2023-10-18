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

class Caracteristicas(models.Model):
    estudante_de_veterinaria=models.BooleanField(default=False)
    medico_veterinario=models.BooleanField(default=False)
    capacidade_adestramento=models.BooleanField(default=False)
    aceita_multiplos_pets=models.BooleanField(default=False)
    cuidador_comum=models.BooleanField(default=False)
    pet_ate_5kg=models.BooleanField(default=False)
    pet_5kg_a_10kg=models.BooleanField(default=False)
    pet_10kg_a_20kg=models.BooleanField(default=False)
    pet_20kg_a_40kg=models.BooleanField(default=False)
    so_pet_castrado=models.BooleanField(default=False)
    pet_nao_castrado=models.BooleanField(default=False)
    pet_femea=models.BooleanField(default=False)
    pet_macho=models.BooleanField(default=False)
    medicacao_oral=models.BooleanField(default=False)
    medicacao_injetavel=models.BooleanField(default=False)

class AvaliacaoCuidador(models.Model):
    nota=models.IntegerField()
    comentario=models.TextField()
    data_hora=models.DateTimeField()

class Imagens(models.Model):
    fotos_local=models.ImageField()