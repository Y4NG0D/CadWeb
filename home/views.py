from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.http import JsonResponse
from django.apps import apps

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

################# PRODUTO ###################

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

def ajustar_estoque(request, id):
    produto = produto = Produto.objects.get(pk=id)
    estoque = produto.estoque # pega o objeto estoque relacionado ao produto
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque)
        if form.is_valid():
            estoque = form.save()
            lista = []
            lista.append(estoque.produto) 
            return render(request, 'produto/lista.html', {'lista': lista})
    else:
         form = EstoqueForm(instance=estoque)
    return render(request, 'produto/estoque.html', {'form': form,})

################# TESTE ###################

def teste1(request):
    return render(request, 'testes/teste1.html')

def teste2(request):
    return render(request, 'testes/teste2.html')

def buscar_dados(request, app_modelo):
    termo = request.GET.get('q', '') # pega o termo digitado
    try:
        # Divida o app e o modelo
        app, modelo = app_modelo.split('.')
        modelo = apps.get_model(app, modelo)
    except LookupError:
        return JsonResponse({'error': 'Modelo não encontrado'}, status=404)
    
    # Verifica se o modelo possui os campos 'nome' e 'id'
    if not hasattr(modelo, 'nome') or not hasattr(modelo, 'id'):
        return JsonResponse({'error': 'Modelo deve ter campos "id" e "nome"'}, status=400)
    
    resultados = modelo.objects.filter(nome__icontains=termo)
    dados = [{'id': obj.id, 'nome': obj.nome} for obj in resultados]
    return JsonResponse(dados, safe=False)

def teste3(request):
    return render(request, 'testes/teste3.html')

#################PEDIDO####################

def pedido(request):
    listaPedido = Pedido.objects.all().order_by('-id')
    return render(request, 'pedido/lista.html', {'listaPedido': listaPedido})

def novo_pedido(request, id):
    # Tentando obter o pedido
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        messages.error(request, 'Pedido não encontrado')
        return redirect('pedido_list')  # Redireciona caso o pedido não exista

    if request.method == 'POST':
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            # Adicionando o item ao pedido
            item_pedido = form.save(commit=False)
            item_pedido.pedido = pedido  # Associando o item ao pedido
            item_pedido.save()
            messages.success(request, 'Produto adicionado com sucesso')
            return redirect('detalhes_pedido', id=pedido.id)  # Redireciona para os detalhes do pedido após salvar
        else:
            messages.error(request, 'Erro ao adicionar o produto ao pedido')
            # Adicionando o print aqui para depurar o que está sendo enviado no form
            print(form.errors)
            return redirect('detalhes_pedido', id=pedido.id)  # Em caso de erro, redireciona para os detalhes do pedido
    
    else:  # GET request
        form = ItemPedidoForm()  # Cria um formulário vazio para exibir
    
    # O contexto de dados para o template
    contexto = {
        'pedido': pedido,
        'form': form
    }
    
    # Retorna o render com o template 'detalhes.html'
    return render(request, 'pedido/detalhes.html', contexto)

def detalhe_pedido(request, id):
    pedido = get_object_or_404(Pedido, pk=id)

    if request.method == "POST":
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            item_pedido = form.save(commit=False)
            item_pedido.pedido = pedido  # Associa o item ao pedido correto
            item_pedido.save()
            messages.success(request, "Produto adicionado ao pedido com sucesso!")
            return redirect('detalhe_pedido', id=pedido.id)
        else:
            messages.error(request, "Erro ao adicionar o produto ao pedido.")

    else:
        form = ItemPedidoForm(initial={'pedido': pedido})

    return render(request, 'pedido/detalhes.html', {'pedido': pedido, 'form': form})

def editar_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=id)

    pedido = item_pedido.pedido  # Obtém o pedido associado ao item
    quantidade_anterior = item_pedido.qtde  # Armazena a quantidade anterior
    produto = item_pedido.produto  # Produto associado ao item
    estoque_atual = produto.estoque.qtde  # Obtém o estoque atual do produto

    if request.method == 'POST':
        form = ItemPedidoForm(request.POST, instance=item_pedido)
        if form.is_valid():
            nova_quantidade = form.cleaned_data['qtde']  # Obtém a nova quantidade solicitada
            
            if nova_quantidade > quantidade_anterior:  # Se o cliente quer mais unidades
                diferenca = nova_quantidade - quantidade_anterior
                if diferenca > estoque_atual:
                    messages.error(request, 'Quantidade em estoque insuficiente para o produto.')
                else:
                    produto.estoque.qtde -= diferenca  # Reduz o estoque
                    produto.estoque.save()
                    item_pedido.save()
                    messages.success(request, 'Produto atualizado com sucesso!')
                    return redirect('detalhes_pedido', id=pedido.id)
            
            elif nova_quantidade < quantidade_anterior:  # Se o cliente quer menos unidades
                diferenca = quantidade_anterior - nova_quantidade
                produto.estoque.qtde += diferenca  # Reabastece o estoque
                produto.estoque.save()
                item_pedido.save()
                messages.success(request, 'Produto atualizado com sucesso!')
                return redirect('detalhes_pedido', id=pedido.id)
            
            else:
                messages.info(request, 'Nenhuma alteração foi feita.')

    else:
        form = ItemPedidoForm(instance=item_pedido)

    contexto = {
        'pedido': pedido,
        'form': form,
        'item_pedido': item_pedido,
    }
    return render(request, 'pedido/detalhes.html', contexto)

def remover_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido')  # Redireciona para a listagem de pedidos caso não encontre o item

    pedido_id = item_pedido.pedido.id  # Armazena o ID do pedido antes de remover o item
    produto = item_pedido.produto  # Obtém o produto relacionado ao item
    estoque = produto.estoque  # Obtém o estoque do produto

    if estoque:
        estoque.qtde += item_pedido.qtde  # Reintegra a quantidade do item ao estoque
        estoque.save()  # Salva as alterações no estoque

    item_pedido.delete()  # Remove o item do pedido
    messages.success(request, 'Item removido com sucesso e estoque atualizado!')

    return redirect('detalhes_pedido', id=pedido_id)  # Retorna à página do pedido


def detalhes_pedido(request, id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido')  
    
    if request.method == 'GET':
        itemPedido = ItemPedido(pedido=pedido)
        form = ItemPedidoForm(instance=itemPedido)
    else:  # Método POST
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            item_pedido = form.save(commit=False)
            produto = item_pedido.produto  # Acessa o produto relacionado
            estoque_atual = produto.estoque.qtde  # Obtém a quantidade atual do estoque
            
            if item_pedido.qtde > estoque_atual:
                messages.error(request, 'Estoque insuficiente para a quantidade solicitada.')
            else:
                item_pedido.preco = produto.preco  # Define o preço do item com base no produto
                produto.estoque.qtde -= item_pedido.qtde  # Atualiza a quantidade do estoque
                produto.estoque.save()  # Salva a atualização no banco de dados
                item_pedido.save()  # Salva o item do pedido
                messages.success(request, 'Produto adicionado com sucesso!')
                return redirect('detalhes_pedido', id=pedido.id)  # Redireciona para evitar reenvio do formulário

        else:
            messages.error(request, 'Erro ao adicionar produto.')

    contexto = {
        'pedido': pedido,
        'form': form,
    }
    return render(request, 'pedido/detalhes.html', contexto)