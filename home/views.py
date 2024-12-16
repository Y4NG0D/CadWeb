from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
            salvando = form.save()
            lista=[]
            lista.append(salvando)
            messages.success(request, 'Operação realizda com Sucesso.')
            return render(request, 'categoria/lista.html', {'lista':lista,})
        
    else: 
        form = CategoriaForm()
    
    return render(request, 'categoria/forms.html', {'form': form,})

def editarCat(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)  # Usa o pk recebido
    except Categoria.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()  # Salva o formulário
            return redirect('lista')  # Redireciona para a lista de categorias

    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'categoria/forms.html', {'form': form})

def deletarCat(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
        categoria.delete()
        messages.success(request, 'Exclusão realizada com sucesso.')
    except Categoria.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')
    except Exception as e:
        messages.error(request, f'Ocorreu um erro inesperado: {e}')
        return redirect('lista')
    
    return redirect('lista')


def detalheCat(request, pk, id):
    try:
        categoria = get_object_or_404(Categoria, pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')

    return render(request, 'categoria/detalhe.html', {'categoria':categoria,})
