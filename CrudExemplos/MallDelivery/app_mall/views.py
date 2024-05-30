from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView

from .models import  Produto, Lojista
from django.urls import reverse_lazy
 
class ProdutoList(ListView): 

    model = Produto 

    template_name = "app_mall/index.html" 




class LojistaCreateView(CreateView):
    model = Lojista
    fields = ['nome', 'CPF', 'telefone', 'email']
    template_name = 'cadastro_lojista.html'
    success_url = reverse_lazy('cadastro_lojista')