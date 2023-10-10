from django.contrib import admin

# Register your models here.

from .models import Pessoa, Cuidador, Tutor, AvaliacaoTutor

admin.site.register(Cuidador)
admin.site.register(Tutor)
admin.site.register(AvaliacaoTutor)