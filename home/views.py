from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.http import JsonResponse
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def categoria(request): 
    contexto = {
        'lista': Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria/lista.html', contexto)

@login_required
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

@login_required
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

@login_required
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

@login_required
def detalheCat(request, id):
    try:
        categoria = get_object_or_404(Categoria, pk=id)
    except Cliente.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')

    return render(request, 'categoria/detalhe.html', {'categoria':categoria,})

@login_required
def cliente(request):
    contexto={
        'listaCliente': Cliente.objects.all().order_by('-id')
    }
    return render(request,'cliente/lista.html', contexto)

@login_required
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

@login_required
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

@login_required
def remover_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()
        messages.success(request, 'Exclusão realizada com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaCliente')
    
    return redirect('listaCliente')

@login_required
def detalhe_cliente(request, id):
    try:
        cliente = get_object_or_404(Cliente, pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaCliente')

    return render(request, 'cliente/detalhes.html', {'cliente':cliente,})

################# PRODUTO ###################

@login_required
def produto(request):
    contexto = {
        'listaProduto': Produto.objects.all().order_by('-id')
    }
    return render(request, 'produto/lista.html', contexto)

@login_required
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

@login_required
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

@login_required
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

@login_required
def detalhe_produto(request, id):
    try:
        produto = get_object_or_404(Produto, pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaProduto')

    return render(request, 'produto/detalhes.html', {'produto': produto})

@login_required
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

@login_required
def teste1(request):
    return render(request, 'testes/teste1.html')

@login_required
def teste2(request):
    return render(request, 'testes/teste2.html')

@login_required
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

@login_required
def teste3(request):
    return render(request, 'testes/teste3.html')

#################PEDIDO####################

@login_required
def pedido(request):
    listaPedido = Pedido.objects.all().order_by('-id')
    return render(request, 'pedido/lista.html', {'listaPedido': listaPedido})

@login_required
def novo_pedido(request,id):
    if request.method == 'GET':
        try:
            cliente = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            # Caso o registro não seja encontrado, exibe a mensagem de erro
            messages.error(request, 'Registro não encontrado')
            return redirect('cliente')  # Redireciona para a listagem
        # cria um novo pedido com o cliente selecionado
        pedido = Pedido(cliente=cliente)
        form = PedidoForm(instance=pedido)# cria um formulario com o novo pedido
        return render(request, 'pedido/form.html',{'form': form,})
    else: # se for metodo post, salva o pedido.
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            
            return redirect('detalhes_pedido', id=pedido.pk)

    return render(request, 'pedido/form.html', {'form': form})

@login_required
def detalhes_pedido(request, id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido')  # Redireciona para a listagem    
    
    if request.method == 'GET':
        itemPedido = ItemPedido(pedido=pedido)
        form = ItemPedidoForm(instance=itemPedido)
    else:  # method Post
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            item_pedido = form.save(commit=False)  # commit=False permite modificações antes de salvar
            item_pedido.preco = item_pedido.produto.preco  # Acessando o preço do produto relacionado
            estoque_atual = item_pedido.produto.estoque
            
            # Verificação do estoque
            print (f'Quantidade pedido: {item_pedido.qtde}')
            print (f'Estoque: {estoque_atual.qtde}')
            if item_pedido.qtde > estoque_atual.qtde:
                messages.error(request, 'Estoque insuficiente para este produto')
            else:
                # Decrementando a quantidade do estoque
                estoque_atual.qtde = estoque_atual.qtde - item_pedido.qtde
                item_pedido.produto.estoque.qtde = estoque_atual
                item_pedido.produto.estoque.save()   # Salvando a atualização do estoque
                item_pedido.save()  # Salvando o item do pedido
                print (f'atualizado: {estoque_atual.qtde}')

                messages.success(request, 'Produto adicionado com sucesso!')
                itemPedido = ItemPedido(pedido=pedido)
                form = ItemPedidoForm(instance=itemPedido)
        else:
            messages.error(request, 'Erro ao adicionar produto')


    contexto = {
        'pedido': pedido,
        'form': form,
    }
    return render(request, 'pedido/detalhes.html', contexto)

@login_required
def editar_pedido(request, id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaPedido')

    if (request.method == 'POST'):
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            produto = form.save()
            listaPedido=[]
            listaPedido.append(produto)
            # return render(request, 'produto/lista.html', {'listaProduto':listaProduto,})
            return redirect('listaPedido')

    else: 
        form = PedidoForm(instance=pedido)
    
    return render(request, 'pedido/form.html', {'form':form,})

@login_required
def remover_item_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=id)
    
    pedido_id = item_pedido.pedido.id  # Armazena o ID do pedido antes de remover o item
    estoque = item_pedido.produto.estoque  # Obtém o estoque do produto
    estoque.qtde += item_pedido.qtde  # Devolve a quantidade do item ao estoque
    estoque.save()  # Salva as alterações no estoque
    # Remove o item do pedido
    item_pedido.delete()
    messages.success(request, 'Operação realizada com Sucesso')


    # Redireciona de volta para a página de detalhes do pedido
    return redirect('detalhes_pedido', id=pedido_id)

@login_required
def remover_pedido(request, id):
    try:
        pedido = Pedido.objects.get(pk=id)
        pedido.delete()
        messages.success(request, 'Exclusão realizda com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaPedido')
    
    return redirect('listaPedido')

@login_required
def editar_item_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=id)
         
    pedido = item_pedido.pedido  # Acessa o pedido diretamente do item
    quantidade_anterior = item_pedido.qtde  # Armazena a quantidade anterior
    if request.method == 'POST':
        form = ItemPedidoForm(request.POST, instance=item_pedido)
        if form.is_valid():
            item_pedido = form.save(commit=False)  # prepara a instância do item_pedido sem persistir ainda
            print(item_pedido.produto.id)

            nova_quantidade_item = item_pedido.qtde
            estoque_atual = item_pedido.produto.estoque.qtde

            if estoque_atual >= nova_quantidade_item:
                estoque_atual = estoque_atual + quantidade_anterior  
                estoque_atual = estoque_atual - nova_quantidade_item

                item_pedido.produto.estoque.qtde = estoque_atual

                item_pedido.produto.estoque.save()
                item_pedido.save()
                messages.success(request, 'Operação realizada com Sucesso')

            else:
                messages.success(request, 'Quantidade em estoque insuficiente para o produto.')

            # realizar aqui o tratamento do estoque
            # Pegar a nova quantidade do item pedido
            # Obtém o estoque atual do produto
            # Verifica se há estoque suficiente para a nova quantidade
            # Se não mostras msg Quantidade em estoque insuficiente para o produto.
            # Se sim
            # Pegar a quantidade anterior ao estoque
            # Decrementa a nova quantidade do estoque
            # Salva as alterações no estoque
            # Salva o item do pedido após ajustar o estoque

            return redirect('detalhes_pedido', id=pedido.id)
    else:
        form = ItemPedidoForm(instance=item_pedido)
        
    contexto = {
        'pedido': pedido,
        'form': form,
        'item_pedido': item_pedido,
    }
    return render(request, 'pedido/detalhes.html', contexto)

@login_required
def editar_item_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=id)

    pedido = item_pedido.pedido  # Obtém o pedido relacionado
    quantidade_anterior = item_pedido.qtde  # Armazena a quantidade anterior do item

    if request.method == 'POST':
        form = ItemPedidoForm(request.POST, instance=item_pedido)
        if form.is_valid():
            item_pedido_editado = form.save(commit=False)  # Prepara o item atualizado sem salvar ainda
            
            nova_quantidade_item = item_pedido_editado.qtde  # Nova quantidade do item
            estoque_item = Estoque.objects.get(produto=item_pedido.produto)  # Obtém o estoque do produto
            
            # Recalculando o estoque corretamente
            estoque_item.qtde += quantidade_anterior  # Devolvendo a quantidade anterior ao estoque
            if estoque_item.qtde >= nova_quantidade_item:
                estoque_item.qtde -= nova_quantidade_item  # Retirando a nova quantidade do estoque
                
                estoque_item.save()  # Salva a atualização no estoque
                item_pedido_editado.save()  # Agora salva o item atualizado
                messages.success(request, 'Operação realizada com sucesso')
            else:
                messages.error(request, 'Quantidade em estoque insuficiente para o produto.')
                return redirect('detalhes_pedido', id=pedido.id)

            return redirect('detalhes_pedido', id=pedido.id)

    else:
        form = ItemPedidoForm(instance=item_pedido)

    contexto = {
        'pedido': pedido,
        'form': form,
        'item_pedido': item_pedido,
    }
    return render(request, 'pedido/detalhes.html', contexto)

@login_required
def form_pagamento(request,id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido')  # Redireciona para a listagem    
    
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Operação realizada com Sucesso')

            pagamento = Pagamento(pedido=pedido)
            form = PagamentoForm(instance=pagamento)
    else: 
        pagamento = Pagamento(pedido=pedido)
        form = PagamentoForm(instance=pagamento)
        
        
    # prepara o formulário para um novo pagamento

    contexto = {
        'pedido': pedido,
        'form': form,
    }    
    return render(request, 'pedido/pagamento.html',contexto)

@login_required
def editar_pagamento(request, id):
    try:
        pagamento = Pagamento.objects.get(pk=id)
        pagamento_id = pagamento.pedido.id
        quantidade_anterior_paga = pagamento.valor  # Armazena a quantidade anterior
        print(f'anteiror: {quantidade_anterior_paga}')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('form_pagamento', id=pagamento_id)

    if (request.method == 'POST'):
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            pagamento_atual = pagamento.pedido.total
            print(f'soma: {pagamento_atual}')

            pagamento_atual = pagamento_atual - pagamento.valor

            print(f'Final: {pagamento_atual}')
            form.save()
            messages.success(request, "Pagamento atualizado com sucesso!")
            return redirect('form_pagamento', id=pagamento_id)
            # return render(request, 'produto/lista.html', {'listaProduto':listaProduto,})
        else:
            messages.success(request, "Pagamento atualizado com sucesso!")

    else: 
        form = PagamentoForm(instance=pagamento)
    
    return render(request, 'pedido/pagamento.html', {'form':form,})

@login_required
def remover_pagamento(request, id):
    try:
        pagamento = Pagamento.objects.get(pk=id)
        pagamento.delete()
        messages.success(request, 'Exclusão realizda com Sucesso.')
        pagamento_id = pagamento.pedido.id
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('form_pagamento', id=pagamento_id)
    
    return redirect('form_pagamento', id=pagamento_id)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')