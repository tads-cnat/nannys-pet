from django import forms
from .models import SolicitacaoHospedagem, Pet, Cuidador

class SolicitacaoHospedagemForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(user=user)
        self.fields['cuidador'].queryset = Cuidador.objects.exclude(user = user.id)

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

class CustomClearableFileInput(forms.ClearableFileInput):
    def get_template_substitution_values(self, value):
        values = super().get_template_substitution_values(value)
        values['clear_checkbox_label'] = "Selecione uma imagem"
        return values
    

class PetForm(forms.ModelForm):
    foto = forms.ImageField(widget=CustomClearableFileInput())

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        self.fields["foto"].label = "Foto do seu Pet"

    class Meta:
        model = Pet
        fields = ['nome', 'idade', 'porte', 'especie', 'docil', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'pet-nome-dialog', 'placeholder': 'Nome do Pet'}),
            'idade': forms.NumberInput(attrs={'class': 'pet-idade'}),
            'porte': forms.Select(attrs={'class': 'pet-porte'}),
            'especie': forms.Select(attrs={'class': 'pet-especie'}),
            'docil': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'pet-foto'}),
        }
