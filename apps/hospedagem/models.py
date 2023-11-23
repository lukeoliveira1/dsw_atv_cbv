from django.db import models

from apps.cliente.models import Cliente
from apps.quarto.models import Quarto

# Create your models here.  
class Hospedagem(models.Model):
    data_entrada = models.DateField()
    data_saida = models.DateField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cliente} - {self.quarto}'
    
class Consumo(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    valor = models.FloatField()
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome