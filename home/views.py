from django.shortcuts import render, redirect

from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

def categoria(request): 
    contexto = {
        'lista': Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria/lista.html', contexto)

def formsCat(request):
    if (request.method == 'POST'):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.nome = form.data['nome']
            categoria.ordem = form.data['ordem']
            categoria.save()
            return redirect('lista')
    else: 
        form = CategoriaForm()
    
    contexto = {
        'form': form,
    }
    return render(request, 'categoria/forms.html', contexto)

def editarCat(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if (request.method == 'POST'):
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.nome = form.data['nome']
            categoria.ordem = form.data['ordem']
            categoria.save()
            return redirect('lista')
    else: 
        form = CategoriaForm(instance=categoria)
    
    contexto = {
        'form': form,
    }
    return render(request, 'categoria/forms.html', {'form':form,})

def deletarCat(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    categoria.delete()
    form = CategoriaForm()
    return  render(request, 'categoria/lista.html')

def detalheCat(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    form = CategoriaForm(instance=categoria)
    contexto = {
        'form': form,
    }
    return render(request, 'categoria/detalhe.html', contexto)