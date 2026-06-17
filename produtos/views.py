from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/listar_produtos.html'
    context_object_name = 'produtos'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produtos/cadastrar_produto.html'
    fields = ['nome', 'descricao', 'preco', 'quantidade', 'ativo']
    success_url = reverse_lazy('listar_produtos')

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/detalhe_produto.html'
    context_object_name = 'produto'