from django.db import models


# Create your models here.
class Academia(models.Model):
    PLANO_CHOICES = (
        ("Mensal", "Mensal"),
        ("Semestral", "Semestral"),
        ("Anual", "Anual"),
    )

    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15)
    plano = models.CharField(
        max_length=10, choices=PLANO_CHOICES, default="Mensal"
    )
    nascimento = models.DateField(blank=True, null=True)
    foto = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.nome
