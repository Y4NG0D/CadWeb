from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/lista/', views.categoria, name="lista"),
    path('categoria/forms/', views.formsCat, name='formsCat'),
    path('editarCat/<int:id>', views.editarCat, name='editarCat'),
    path('categoria/detalheCat/<int:id>/', views.detalheCat, name='detalheCat'),
    path('deletarCat/<int:id>/', views.deletarCat, name='deletarCat'),
    ########## Cliente ##########
    path('cliente/lista', views.cliente, name='listaCliente'),
    path('cliente/formulario', views.form_cliente, name='form_cliente'),
    path('detalhe_cliente/<int:id>', views.detalhe_cliente, name='detalhe_cliente'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>/', views.remover_cliente, name='remover_cliente'),
    ########## Produto ##########
    path('produto/lista/', views.produto, name='listaProduto'),
    path('produto/formulario', views.form_produto, name='form_produto'),
    path('editar_produto/<int:id>/', views.editar_produto, name='editar_produto'),
    path('remover_produto/<int:id>/', views.remover_produto, name='remover_produto'),
    path('detalhe_produto/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
    ########## Estoque ##########
    path('ajustar_estoque/<int:id>', views.ajustar_estoque, name='ajustar_estoque'),
    ########## Teste ##########
    path('teste1/', views.teste1, name='teste1'),
    path('teste2/', views.teste2, name='teste2'),
    path('buscar_dados/<str:app_modelo>/', views.buscar_dados, name='buscar_dados'),
    path('teste3/', views.teste3, name='teste3'),
    ########## Pedido ##########
    path('buscar_dados/<str:app_modelo>/', views.buscar_dados, name='buscar_dados'),
    path('pedido', views.pedido, name="pedido"),
    path('novo_pedido/<int:id>', views.novo_pedido, name='novo_pedido'),
    path('remover_pedido/<int:id>', views.remover_pedido, name='remover_pedido'),
    path('detalhes_pedido/<int:id>', views.detalhes_pedido, name='detalhes_pedido'),
    path('detalhes_pedido/<int:id>/editar', views.editar_item_pedido, name='editar_item_pedido'),
    path('detalhes_pedido/remover_item/<int:id>/', views.remover_item_pedido, name='remover_item_pedido'),
    path('form_pagamento/<int:id>/', views.form_pagamento, name='form_pagamento'),
    path('pagamento/editar/<int:id>/', views.editar_pagamento, name='editar_pagamento'),
    path('pagamento/remover/<int:id>/', views.remover_pagamento, name='remover_pagamento'),
]