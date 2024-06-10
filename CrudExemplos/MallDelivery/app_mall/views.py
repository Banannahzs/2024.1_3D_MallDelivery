from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import  Produto, Lojista, Loja
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q
 
class ProdutoList(ListView): 

    model = Produto 
    template_name = "lista_produtos.html" 
    context_object_name = 'produtos'


class LojistaList(ListView): 

    model = Lojista
    template_name = "app_mall/lista_lojista.html" 
    context_object_name = 'lojistas'

class LojaList(ListView): 

    model = Loja
    template_name = "app_mall/lista_loja.html" 
    context_object_name = 'lojas'
    
class LojistaCreateView(LoginRequiredMixin, CreateView):
    model = Lojista
    fields = ['nome', 'CPF', 'telefone', 'email']
    template_name = 'cadastro_lojista.html'
    success_url = reverse_lazy('cadastro_lojista')

class LojistaUpdateView(LoginRequiredMixin, UpdateView):
    model = Lojista
    fields = ['nome', 'CPF', 'telefone', 'email']
    template_name = 'update_lojista.html'
    success_url = reverse_lazy('lista_lojista')

class LojistaDeleteView(LoginRequiredMixin, DeleteView):
    model = Lojista
    template_name = 'lojista_confirm_delete.html'
    success_url = reverse_lazy('lista_lojista')

class LojaCreateView(LoginRequiredMixin, CreateView):
    model = Loja
    fields = ['nome', 'cnpj', 'descricao', 'lojista']
    template_name = 'cadastro_loja.html'
    success_url = reverse_lazy('cadastro_loja')

class LojaUpdateView(LoginRequiredMixin, UpdateView):
    model = Loja
    fields = ['nome', 'cnpj', 'descricao', 'lojista']
    template_name = 'update_loja.html'
    success_url = reverse_lazy('lista_loja')

class LojaDeleteView(LoginRequiredMixin, DeleteView):
    model = Loja
    template_name = 'loja_confirm_delete.html'
    success_url = reverse_lazy('lista_loja')

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'preco', 'descricao', 'estoque', 'categoria', 'loja']
    template_name = 'add_produto.html'
    success_url = reverse_lazy('add_produto')

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'preco', 'descricao', 'estoque', 'categoria', 'loja']
    template_name = 'update_produto.html'
    success_url = reverse_lazy('index')

class ProdutoDeleteView(LoginRequiredMixin, DeleteView): 

    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('index')

def feed_produtos(request):
    produto = Produto.objects.all()
    categoria = Produto.objects.values_list('categoria', flat=True).distinct()
    
    query = request.GET.get('search')
    sort_by = request.GET.get('sort_by', 'nome')  # Default sort field is 'nome'
    filter_by = request.GET.get('filter_by', None)  # Default filter field is None
    
    if query:
        produto_list = Produto.objects.filter(Q(nome__icontains=query))
    else:
        produto_list = Produto.objects.all()
    
    if filter_by:
        produto_list = produto_list.filter(categoria=filter_by)

    produto_list = produto_list.order_by(sort_by)
    
        
    # Pagination Code    
    paginator = Paginator(produto_list, 4)  # Show 10 empregados per page.
    page_number = request.GET.get('page')
    produto = paginator.get_page(page_number)
    
    return render(request, 'app_mall/index.html', {'produtos': produto, 'categoria': categoria})
