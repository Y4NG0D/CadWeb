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
]   