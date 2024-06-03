from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, DeleteView

from .models import  Produto, Lojista, Loja
from django.urls import reverse_lazy
 
class ProdutoList(ListView): 

    model = Produto 
    template_name = "app_mall/index.html" 
    context_object_name = 'produtos'


class LojistaList(ListView): 

    model = Lojista
    template_name = "app_mall/lista_lojista.html" 
    context_object_name = 'lojistas'

class LojaList(ListView): 

    model = Loja
    template_name = "app_mall/lista_loja.html" 
    context_object_name = 'lojas'

class LojistaCreateView(CreateView):
    model = Lojista
    fields = ['nome', 'CPF', 'telefone', 'email']
    template_name = 'cadastro_lojista.html'
    success_url = reverse_lazy('cadastro_lojista')

class LojaCreateView(CreateView):
    model = Loja
    fields = ['nome', 'cnpj', 'descricao', 'lojista']
    template_name = 'cadastro_loja.html'
    success_url = reverse_lazy('cadastro_loja')

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'preco', 'descricao', 'estoque', 'categoria', 'loja']
    template_name = 'add_produto.html'
    success_url = reverse_lazy('add_produto')

class ProdutoDeleteView(DeleteView): 

    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('index')

