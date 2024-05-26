from django.db import models
from django.core.validators import RegexValidator


class Lojista(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, validators=[RegexValidator(regex='^\d{11}$', message='CPF deve ter 11 dígitos')])
    telefone = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


    
class Loja(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    descricao = models.TextField(blank=True, null=True)
    lojista = models.ForeignKey(Lojista, related_name='lojas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)
    loja = models.ForeignKey(Loja, related_name='loja', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


