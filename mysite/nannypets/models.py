import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Pet(models.Model):
    nome = models.CharField(max_length=255)
    



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

# class Pet(models.Model):
#    nome = models.CharField(max_length=200)
#    idade = models.IntegerField(default=0)
#    porte = models.CharField(max_length=200)
#    docil = models.BooleanField()
#    especie = models.CharField(max_length=200)

# class Cuidador(models.Model):
#    dia_disponivel = models.CharField(max_length=200)
#    valor_diaria = models.IntegerField(default=1)
#    preferencia_porte = models.CharField(max_length=200)

# class Hospedagem(models.Model):
#    status = models.CharField(max_length=200)
#    data_inicial = models.DateTimeField()
#    data_final = models.DateTimeField()

# Create your models here.
