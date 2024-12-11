from django.forms import ModelForm
from django import forms
from .models import *

class CategoriaForm(forms.ModelForm):
     class Meta:
          model = Categoria
          fields = ['nome', 'ordem',]
          exclude = ['senha',]
          widgets = {
               'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome', 'style': 'margin-bottom::15px'}),
               'ordem': forms.NumberInput(attrs={'class': 'inteiro form-control', 'placeholder': 'Ordem'}),
          }
          labels = {
               'nonme': 'Informe o nome do produto: ',
               'ordem': 'Informe o número da ordem: ',
          }