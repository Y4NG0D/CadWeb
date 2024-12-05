from django.forms import ModelForm
from .models import *

class CategoriaForm(ModelForm):
     class Meta:
          model = Categoria
          fields = ['nome', 'ordem']