import re
from django.db import models
from django.core import validators
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from datetime import datetime, timedelta


class Pet(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    ESPECIE = (1, 'Cachorro'), (2,'Gato')
    TAMANHO = (1, 'Porte pequeno'), (2, 'Porte médio'), (3, 'Porte grande')
    porte = models.IntegerField(choices=TAMANHO,)
    especie = models.IntegerField(choices=ESPECIE,)
    docil = models.BooleanField()
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pet_photos',
                             blank=True)
    def __str__(self):
        return self.nome

class Cuidador(models.Model):
    DIAS = (1, 'Domingo'), (2, 'Segunda-feira'), (3, 'Terça-feira'), (4, 'Quarta-feira'), (5, 'Quinta-feira'), (6, 'Sexta-feira'), (7, 'Sábado')
    PORTES = (1, 'Pequeno porte'), (2, 'Médio porte'), (3, 'Grande porte')
    dias_disponiveis = models.IntegerField(choices=DIAS)
    valor_diaria = models.IntegerField(default=1)
    preferencia_porte = models.IntegerField(choices=PORTES)
    User = settings.AUTH_USER_MODEL
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True,  
    )
    def __str__(self):
        return self.user.username    

class SolicitacaoHospedagem(models.Model):
    STATUS = (0, 'Aguardando'), (1, 'Rejeitada'), (2, 'Confirmada')
    status = models.IntegerField(choices=STATUS, default=0)
    dia_inicial = models.DateField("Data Inicial")
    dia_final = models.DateField("Data final")
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Solicitação {self.id} - Usuário: {self.user.username} & Pet: {self.pet.nome} -> Cuidador: {self.cuidador.user.username}' 


class Hospedagem(models.Model):
    SITUACAO = (0, 'Em andamento'), (1, 'Concluída')
    situacao = models.IntegerField(choices=SITUACAO, default=0)
    solicitacao_hospedagem = models.OneToOneField(
        SolicitacaoHospedagem, 
        on_delete=models.CASCADE,
        primary_key=True,  
    )
    def __str__(self):
        return f'Hospedagem {self.solicitacao_hospedagem.id} - Pet: {self.solicitacao_hospedagem.pet.nome} & Dono: {self.solicitacao_hospedagem.user.username} | Cuidador: {self.solicitacao_hospedagem.cuidador.user.username}'

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
          raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                 is_staff=is_staff, is_active=True,
                 is_superuser=is_superuser, last_login=now,
                 date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True,
                 **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('username'), max_length=15, unique=True,
        help_text=_('Required. 15 characters or fewer. Letters, \
                    numbers and @/./+/-/_ characters'),
        validators=[
                    validators.RegexValidator(
                                            re.compile('^[\w.@+-]+$'),
                                            _('Enter a valid username.'),
                                            _('invalid'))])
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as active. \
                    Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    foto = models.ImageField(_('foto'), upload_to='user_photos', null=True,
                             blank=True)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',] 

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

# Create your models here.