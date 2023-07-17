from django import forms
from .models import SolicitacaoHospedagem

class SolicitacaoHospedagemForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoHospedagem
        fields = ['dia_inicial', 'dia_final', 'cuidador', 'pet']
        widgets = {
            'dia_inicial': forms.DateInput(attrs={'class': 'data-input'}),
            'dia_inicial': forms.DateInput(attrs={'type': 'date'}),
            'dia_final': forms.DateInput(attrs={'class': 'data-input'}),
            'dia_final': forms.DateInput(attrs={'type': 'date'}),
            'cuidador': forms.Select(attrs={'class': 'cuidador-select'}),
            'pet': forms.Select(attrs={'class': 'pet-select'}),
        }