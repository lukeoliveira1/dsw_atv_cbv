from django.db import models

# Create your models here.
class Quarto(models.Model):
    apartamento = models.IntegerField()
    valor = models.FloatField()

    def __str__(self):
        return str(self.apartamento)