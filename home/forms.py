from django.forms import ModelForm
from django import forms
from .models import *
from datetime import date

class CategoriaForm(forms.ModelForm):
     class Meta:
          model = Categoria
          fields = ['nome', 'ordem',]
          # exclude = ['senha',]  #Exclui campos especificos 
          widgets = {
               'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome', 'style': 'margin-bottom::15px'}),
               'ordem': forms.NumberInput(attrs={'class': 'inteiro form-control', 'placeholder': 'Ordem'}),
          }
          labels = {
               'nonme': 'Informe o nome do produto: ',
               'ordem': 'Informe o número da ordem: ',
          }

     def clean_nome(self):
          nome = self.cleaned_data.get('nome')
          if not self.instance.pk:  # Verifica se exite id, caso não exita verificar o valor colocado se já existe ou não
               if Categoria.objects.filter(nome=nome).exists():
                    raise forms.ValidationError("Já existe uma categoria com esse mesmo nome.")
          if len(nome) < 3:
               raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")          
          return nome
     
     def clean_ordem(self):
          ordem = self.cleaned_data.get('ordem')
          if not self.instance.pk:
               if Categoria.objects.filter(ordem=ordem).exists():
                    raise forms.ValidationError("O númera da ordem digitada já esta sendo utilizada.")
          if ordem <= 0:
               raise forms.ValidationError("O campo ordem tem que ser superior a 0.")
          return ordem
     



class ClienteForm(forms.ModelForm):
     class Meta:
          model = Cliente 
          fields = ['nome', 'cpf', 'datanasc',]
          widgets = {
               'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
               'cpf':forms.TextInput(attrs={'class': 'cpf form-control', 'placeholder': 'C.P.F'}),
               'datanasc':forms.DateInput(attrs={'class': 'data form-control', 'placeholder': 'Data de Nascimento'}, format='%d/%m/%Y'),
          }

     def clean_nome(self):
          nome = self.cleaned_data.get('nome') #novo valor ao adicionar
          if not self.instance.pk:   # Verifica se exite id, caso não exita verificar o valor colocado se já existe ou não
               if Cliente.objects.filter(nome=nome).exists():
                    raise forms.ValidationError("Já existe um cliente com esse nome.")
          print(nome)
          if self.instance.pk:
               if nome != self.instance.nome:
                    print(self.instance.nome) #valor antigo
                    self.instance.nome = nome  # Atualiza o valor antigo com o novo
                    self.instance.save()  # Salva a alteração no banco
                    self._changed = True  # Marca que houve alteração
               elif len(nome) < 3:
                    raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
               elif Cliente.objects.filter(nome=nome).exists():
                    raise forms.ValidationError("Já existe um cliente com esse nome.")

          
          return nome
     
     
     def clean_cpf(self):
          cpf = self.cleaned_data.get('cpf')
          if not self.instance.pk:
               if Cliente.objects.filter(cpf=cpf).exists():
                    raise forms.ValidationError("Já existe um cliente com esse C.P.F.")

          if self.instance.pk:
               if len(cpf) != 14:
                    raise forms.ValidationError("Esta faltando numero no seu CPF.")
          return cpf
     
     def clean_datanasc(self):
          datanasc = self.cleaned_data.get('datanasc')
          if datanasc >= date.today():
               raise forms.ValidationError("A data de nascimento não pode ser maior que a data atual.")
          return datanasc