from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria, Cliente, Produto
from .forms import CategoriaForm, ClienteForm, ProdutoForm

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
            messages.success(request, 'Operação realizada com Sucesso.')
            return render(request, 'categoria/lista.html', {'lista':lista,})
        
    else: 
        form = CategoriaForm()
    
    return render(request, 'categoria/forms.html', {'form': form,})

def editarCat(request, id):
    try:
        categoria = Categoria.objects.get(id=id)  # Usa o pk recebido
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

def deletarCat(request, id):
    try:
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        messages.success(request, 'Exclusão realizada com sucesso.')
    except Categoria.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')
    except Exception as e:
        messages.error(request, f'Ocorreu um erro inesperado: {e}')
        return redirect('lista')
    
    return redirect('lista')


def detalheCat(request, id):
    try:
        categoria = get_object_or_404(Categoria, pk=id)
    except Cliente.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')

    return render(request, 'categoria/detalhe.html', {'categoria':categoria,})

def cliente(request):
    contexto={
        'listaCliente': Cliente.objects.all().order_by('-id')
    }
    return render(request,'cliente/lista.html', contexto)

def form_cliente(request):
    if (request.method == 'POST'):
        form = ClienteForm(request.POST)
        if form.is_valid():
            salvando = form.save()
            listaCliente=[]
            listaCliente.append(salvando)
            messages.success(request, 'Operação realizada com Sucesso.')
            return render(request, 'cliente/lista.html', {'listaCliente':listaCliente,})
        
    else: 
        form = ClienteForm()
    
    return render(request, 'cliente/formulario.html', {'form': form,})


def editar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaCliente')

    if (request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            listaCliente=[]
            listaCliente.append(cliente)
            return render(request, 'cliente/lista.html', {'listaCliente':listaCliente,})

    else: 
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente/formulario.html', {'form':form,})


def remover_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()
        messages.success(request, 'Exclusão realizada com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaCliente')
    
    return redirect('listaCliente')

def detalhe_cliente(request, id):
    try:
        cliente = get_object_or_404(Cliente, pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaCliente')

    return render(request, 'cliente/detalhes.html', {'cliente':cliente,})

def produto(request):
    contexto = {
        'listaProduto': Produto.objects.all().order_by('-id')
    }
    return render(request, 'produto/lista.html', contexto)

def form_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            salvando = form.save()
            messages.success(request, 'Operação realizada com Sucesso.')
            return redirect('listaProduto')
    else:
        form = ProdutoForm()
    
    return render(request, 'produto/form.html', {'form': form})

def editar_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Produto.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaProduto')

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operação realizada com Sucesso.')
            return redirect('listaProduto')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produto/form.html', {'form': form})

def remover_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
        produto.delete()
        messages.success(request, 'Exclusão realizada com Sucesso.')
    except Produto.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
    except Exception as e:
        messages.error(request, f'Ocorreu um erro inesperado: {e}')
    
    return redirect('listaProduto')

def detalhe_produto(request, id):
    try:
        produto = get_object_or_404(Produto, pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaProduto')

    return render(request, 'produto/detalhes.html', {'produto': produto})
