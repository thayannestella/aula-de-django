from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

