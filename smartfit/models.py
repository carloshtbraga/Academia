from django.db import models


# Create your models here.
class Academia(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    foto = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.nome
