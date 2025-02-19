import locale
from django.db import models
import hashlib
from decimal import Decimal

################### CATEGORIA ###################

class Categoria(models.Model): 
    nome = models.CharField(max_length = 100)
    ordem = models.IntegerField()

    def __str__(self):
        return self.nome
    
################### CLIENTE ###################
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100) 
    cpf = models.CharField(max_length=15,verbose_name="C.P.F")
    datanasc = models.DateField(verbose_name="Data de Nascimento")

    def __str__(self):
        return self.nome
    
    @property
    def datanascimento(self):
          """Retorna a data de nascimento no formato DD/MM/AAAA """
          if self.datanasc:
               return self.datanasc.strftime('%d/%m/%Y')
          return None
    
################### PRODUTO ###################
    
class Produto(models.Model):
     nome = models.CharField(max_length=100)
     preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
     img_base64 = models.TextField(blank=True)

     def __str__(self):
          return self.nome
     
     @property

     def estoque(self):
          estoque_item, flag_create = Estoque.objects.get_or_create(produto=self, defaults={'qtde': 0})
          return estoque_item
     
################### ESTOQUE ###################

class Estoque(models.Model):
     produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
     qtde = models.IntegerField()

     def __str__(self):
          return f'{self.produto.nome} - Quantidade: {self.qtde}'
     
################### PEDIDO ###################

class Pedido(models.Model):

    NOVO = 1
    EM_ANDAMENTO = 2
    CONCLUIDO = 3
    CANCELADO = 4

    STATUS_CHOICES = [
        (NOVO, 'Novo'),
        (EM_ANDAMENTO, 'Em Andamento'),
        (CONCLUIDO, 'Concluído'),
        (CANCELADO, 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=NOVO)

    def __str__(self):
            return f"Pedido {self.id} - Cliente: {self.cliente.nome} - Status: {self.get_status_display()}"
    
    @property
    def data_pedidof(self):
        if self.data_pedido:
            return self.data_pedido.strftime('%d/%m/%Y %H:%M')
        return None

    @property 
    def total(self):
        total = sum(item.qtde * item.preco for item in self.itempedido_set.all())
        return total
    
    @property
    def qtdeItens(self):
        return self.itempedido_set.count()
    
    @property
    def pagamentos(self):
        return Pagamento.objects.filter(pedido=self)

    @property
    def total_pago(self):
        total = sum(pagamento.valor for pagamento in self.pagamentos.all())
        return total
    
    @property
    def debito(self):
        valor_debito = self.total - self.total_pago 
        return valor_debito
    
    @property
    def chave_acesso(self):
        chave_base = f"{self.id}{self.data_pedido.strftime('%Y%m%d%H%M%S')}"
        return hashlib.sha256(chave_base.encode()).hexdigest()[:44]
    
    @property
    def total_pedido(self):
        return sum(item.calculoTotal for item in self.itempedido_set.all())
    
    @property
    def icms(self):
        return self.total_pedido * Decimal('0.18')

    @property
    def pis(self):
        return self.total_pedido * Decimal('0.0165')

    @property
    def ipi(self):
        return self.total_pedido * Decimal('0.05')

    @property
    def cofins(self):
        return self.total_pedido * Decimal('0.076')

    @property
    def total_impostos(self):
        return self.icms + self.pis + self.ipi + self.cofins
    
    @property
    def total_com_impostos(self):
        return self.total_pedido + self.total_impostos
    



class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  
    qtde = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto.nome} (Qtde: {self.qtde}) - Preço Unitário: {self.preco}"
    
    @property
    def calculoTotal(self):
        total = self.qtde * self.preco
        return total

    @property
    def total(self):
        total = sum(item.qtde * item.preco for item in self.itempedido_set.all())
        return total


class Pagamento(models.Model):
    DINHEIRO = 1
    CREDITO = 2
    DEBITO = 3
    PIX = 4
    TICKET = 5
    OUTRA = 6

    FORMA_CHOICES = [
        (DINHEIRO, 'Dinheiro'),
        (CREDITO, 'Credito'),
        (DEBITO, 'Debito'),
        (PIX, 'Pix'),
        (TICKET, 'Ticket'),
        (OUTRA, 'Outra'),
    ]

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE) 
    forma = models.IntegerField(choices=FORMA_CHOICES)
    valor = models.DecimalField(max_digits = 10, decimal_places=2, blank = False )
    data_pgto = models.DateTimeField(auto_now_add=True)

    @property
    def data_pgtof(self):
        """Retorna a data formatada: DD/MM/AAAA HH:MM"""
        if self.data_pgto:
            return self.data_pgto.strftime('%d/%m/%Y %H:%M')
        return None